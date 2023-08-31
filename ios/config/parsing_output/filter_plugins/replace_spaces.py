def replace_space(filename):
    return filename.replace(" ", "_")

class FilterModule:
    def filters(self):
        return {
                "replace_spaces": replace_spaces,
                }
