# 1
def is_starting_with_program_name(program: str, command: str) -> bool: # 명령어가 제대로된 프로그램 이름으로 시작하는지 확인
    if command.startswith(program):
        return True
    return False

def is_valid_command_by_rule(flag_rule_dictionary_by_flag_name: dict, command_to_check: str) -> bool: # 커맨드를 순회하며 flag에 맞는 argument인지 확
    commands_list = list(command_to_check.split())[1:]
    index = 0
    while index < len(commands_list):
        if commands_list[index] in flag_rule_dictionary_by_flag_name:
            flag_rule = flag_rule_dictionary_by_flag_name[commands_list[index]]
            if flag_rule == "STRING":
                if index == len(commands_list)-1 or not commands_list[index+1].isalpha():
                    return False
                index += 2
            elif flag_rule == "NUMBER":
                if index == len(commands_list)-1:
                    return False
                for one_command in commands_list[index+1]:
                    if one_command not in "1234567890":
                        return False
                index += 2
            elif flag_rule == "NULL":
                if index != len(commands_list)-1 and commands_list[index+1] not in flag_rule_dictionary_by_flag_name:
                    return False
                index += 1
        else:
            return False
    return True

def make_flag_rules_dictionary(flag_rules: list) -> dict: # flag_rules를 dictionary로 변경하여 반환
    flag_rules_dictionary_by_flag_name = {}
    for flag_rule in flag_rules:
        flag_name, flag_argument_type = flag_rule.split()
        flag_rules_dictionary_by_flag_name[flag_name] = flag_argument_type
    return flag_rules_dictionary_by_flag_name

def solution(program, flag_rules, commands):
    validation_check_result = [False for _ in range(len(commands))] # 개별 커맨드의 적합도 결과 생성
    flag_rule_dictionary_by_flag_name = make_flag_rules_dictionary(flag_rules) # 주어진 flag_rules를 dictionary로 변경
    for index in range(len(commands)):
        command_to_check = commands[index] # 현재 체크할 커맨드
        if not is_starting_with_program_name(program, command_to_check): # 커맨드가 프로그램 이름으로 시작하지 않으면 잘못된 명령이므로 TRUE로 변경없이 넘어감
            continue
        if is_valid_command_by_rule(flag_rule_dictionary_by_flag_name, command_to_check): # rule에 맞는 커맨드이면 check 결과를 True로 변경
            validation_check_result[index] = True
    return validation_check_result


print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -n 100 -s hi -e", "lien -s Bye"]))
print(solution("line", ["-s STRING", "-n NUMBER", "-e NULL"], ["line -s 123 -n HI", "line fun"]))
