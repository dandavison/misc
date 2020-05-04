class Unknown:
    def respond_to_line(self, line):
        print(line)
        if line.startswith("commit "):
            return CommitMeta()
        elif line.startswith("diff"):
            return FileMeta()
        else:
            return self


state = Unknown()
for line in lines:
    state = state.respond_to_line()
