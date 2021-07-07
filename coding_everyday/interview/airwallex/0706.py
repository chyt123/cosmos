import collections


class CmdEnum:
    FROM = 'FROM'
    SELECT = 'SELECT'
    TAKE = 'TAKE'
    COUNT = 'COUNT'
    SORT = 'SORT'
    JOIN = 'JOIN'


class CSVProcessing:
    def __init__(self):
        self.mem = list()
        self.result = []
        self.take = 0

    def from_csv(self, filename):
        with open(filename, 'r') as f:
            # Process 1st row
            line = f.readline()
            col_names = line.replace('\n', '').split(',')
            self.mem.append(col_names)

            # From 2nd row
            line = f.readline()
            while line:
                info = line.replace('\n', '').split(',')
                self.mem.append(info)
                line = f.readline()
        self.result = self.mem

    def select_csv(self, cols):
        needed = [i for i in range(len(self.result[0])) if self.result[0][i] in cols]
        self.result = [[row[i] for i in needed] for row in self.result]

    def count_csv(self, col):
        self.result = [[col, 'count']]
        idx = self.mem[0].index(col)
        cnt = collections.Counter([i[idx] for i in self.mem[1:]])
        for i in cnt:
            self.result.append([i, str(cnt[i])])

    def print_csv(self, take=None):
        if take is None:
            take = len(self.result) - 1

        for i in range(0, take + 1):
            print(','.join(self.result[i]))


def run(command):
    csv_processing = CSVProcessing()
    cmds = command.split()
    take = None
    for i in range(len(cmds)):
        if cmds[i] == CmdEnum.FROM:
            csv_processing.from_csv(cmds[i + 1])
        if cmds[i] == CmdEnum.TAKE:
            take = int(cmds[i + 1])
        if cmds[i] == CmdEnum.COUNT:
            csv_processing.count_csv(cmds[i + 1])
        if cmds[i] == CmdEnum.SELECT:
            cols = cmds[i + 1].split(',')
            csv_processing.select_csv(cols)

    csv_processing.print_csv(take)


# run("FROM small_countries.csv")
# run("FROM small_countries.csv TAKE 2")
# run("FROM small_countries.csv SELECT country,country_name TAKE 2")
# run("FROM small_countries.csv TAKE 2 SELECT country,country_name")
# run("FROM languages.csv COUNT lang_name SELECT lang_name")
