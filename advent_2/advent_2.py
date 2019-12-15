from entries import entries

class Advent2:
    def __init__(self):
        self.memory = []

    def __repr__(self):
        return 'Advent2 ({!r})'.format(self.memory)

    def get_position_by_pointer(self, pointer):
        return self.memory[pointer]

    def get_value_by_position(self, position):
        return self.memory[position]

    def run_program(self):
        for ins_ptr in range(0, len(self.memory) - 1, 4):
            if self.memory[ins_ptr] == 1:
                parameter_1 = self.get_position_by_pointer(ins_ptr+1)
                parameter_2 = self.get_position_by_pointer(ins_ptr+2)
                parameter_3 = self.get_position_by_pointer(ins_ptr+3)
                self.memory[parameter_3] = self.get_value_by_position(
                    parameter_1) + self.get_value_by_position(parameter_2)
            elif self.memory[ins_ptr] == 2:
                parameter_1 = self.get_position_by_pointer(ins_ptr+1)
                parameter_2 = self.get_position_by_pointer(ins_ptr+2)
                parameter_3 = self.get_position_by_pointer(ins_ptr+3)
                self.memory[parameter_3] = self.get_value_by_position(
                    parameter_1) * self.get_value_by_position(parameter_2)
            elif self.memory[ins_ptr] == 99:
                break
            else:
                break

    def run_combinations(self, input):
        for x in range(99):
            for y in range(99):
                self.memory = list(entries)
                self.memory[1] = x
                self.memory[2] = y
                self.run_program()
                if self.memory[0] == input:
                    return ((x*100) + y)
        return []

print(Advent2().run_combinations(19690720))
