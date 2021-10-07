def create_tuple_lst(lst):
    tuple_lst = []
    for elem in lst:
        tuple_lst.append((elem, ),)
    return tuple_lst


def selection_ques(select_ques, outputs):
    # building looped question
    select_input = "Your Selection: "
    output_loop = ""

    selection_dict = {}

    for count, output in enumerate(outputs):
        count += 1
        output_str = f"{count}) {output[0]}\n"
        output_loop = output_loop+output_str
        selection_dict[count] = output[0]

    selection_ques_str = select_ques+output_loop+select_input

    while (user_input := int(input(selection_ques_str))) != "x":
        if user_input in selection_dict:
            selection = selection_dict.get(user_input)
            break
        else:
            print("Invalid input, please try again!")
    return user_input


# 1) Print Welcome --> Enter to begin
print("Welcome to the tip calculator")


# 2) Get total of bill before tax
tot_bill = float(input("What is the subtotal of your bill? "))

# 3) What state are you in
st_tax = float(input("To calculate tax what State are you in? "))

# 4) Get num people of who will split the bill
num_ppl_split = int(
    input("How many people in your party would you like to split the bill with"))

# 5) Get tip percentage
# tip = float(input("What percentage of tip would you like to add? "))


def live_tip(tot_bill, st_tax):
    select_ques = "What percentage of tip would you like to add?\n"
    tips = [("15%: ", .15), ("20%: ", .20), ("25%: ", .25)]
    selection_lst = []
    for tip in tips:
        bill_calc = round(((tot_bill*(1+st_tax)) * (1+tip[1])), 2)
        selection_lst.append(f"{tip[0]} ${bill_calc}")
    selection_lst.append("Custom")
    outputs = create_tuple_lst(selection_lst)
    user_input = selection_ques(select_ques, outputs)
    return user_input


tip_options = live_tip(tot_bill, st_tax)
print(tip_options)
if tip_options == 1:
    tip = 0.15
elif tip_options == 2:
    tip = .20
elif tip_options == 3:
    tip = .25
elif tip_options == 4:
    tip = float(
        input("Please enter the tip amount you would like to add: "))

final_bill_split = round(
    (((tot_bill*(1+st_tax)) * (1+tip)) / num_ppl_split), 2)
print(f"The final split will be ${final_bill_split} per person.")
