user_admin=int(input("Press 1 for Student \t Press 2 for Admin:"))
if user_admin==1:
    print("Name of student:")
    print("Roll.No.:")
    print("Semester:")
    print("Group No.:")
    print("Your Gmail:")
    
    choose_subject=int(input("Press 1 for BEE. \t Press 2 for CP \t Press 3 for SCM \t Press 0 for Exit:"))
    if choose_subject==1:
        choose_theory_lab=int(input("Press 1 for BE Theory \t Press 2 for BE Lab:"))
        if choose_theory_lab==1:
            A_in_BE_theory=(classes_attended/total_class)*100
            print("Your attendance in BE. Theory:",A_in_BE_theory)
            more_info=int(input("Press 1 for More Info \tPress 0 for Exit:"))
            if more_info==1:
                print("Your attendance in BE theory:",classes_attended)
                print("Total No. of classes in BE thoery:",total_class)
            elif more_info==0:
                exit()
            else:
                print("Type Valid Value")
                
        elif choose_theory_lab==2:
            A_in_BE_lab=(classes_attended/total_class)*100
            print("Your attendance in BE Lab:",A_in_BE_lab)
            more_info=int(input("Press 1 for More Info \tPress 0 for Exit:"))
            if more_info==1:
                print("Your attendance in BE Lab:",classes_attended)
                print("Total No. of classes in BE Lab:",total_class)
            elif more_info==0:
                exit()
            else:
                print("Type Valid Value")
        else: 
            print("Type Valid Value")
    elif choose_subject==2:
        choose_theory_labC=int(input("Press 1 for C Theory \t Press 2 for C Lab:"))
        if choose_theory_labC==1:
            A_in_Ctheory=(classes_attended/total_class)*100
            print("Your attendance in C Theory:",A_in_Ctheory)
            more_info=int(input("Press 1 for More Info \tPress 0 for Exit:"))
            if more_info==1:
                print("Your attendance in C theory:",classes_attended)
                print("Total No. of classes in C thoery:",total_class)
            elif more_info==0:
                exit()
            else:
                print("Type Valid Value")
        elif choose_theory_labC==2:
            A_in_Clab=(classes_attended/total_class)*100
            print("Your attendance in C Lab:",A_in_Clab)
            more_info=int(input("Press 1 for More Info \tPress 0 for Exit:"))
            if more_info==1:
                print("Your attendance in C Lab:",classes_attended)
                print("Total No. of classes in C Lab:",total_class)
            elif more_info==0:
                exit()
            else:
                print("Type Valid Value")
        else:
            print("Type Valid Value")
    elif choose_subject==3:
        A_in_SCM=(classes_attended/total_class)*100
        print("Your attendance in SCM:",A_in_SCM)
        more_info=int(input("Press 1 for More Info \tPress 0 for Exit:"))
        if more_info==1:
            print("Your attendance in SCM:",classes_attended)
            print("Total No. of classes in SCM:",total_class)
        elif more_info==0:
            exit()
        else:
            print("Type Valid Value")
    elif choose_subject==0:
        exit()
    else:
        print("Type Valid Value")

        
        
        
        
        
        
        
        
        
        
elif user_admin==2:
    user_name=input("Type your Email:")
    password=int(input("Type your Password:"))
    if user_name=="Name@gmail.com" and password==123:
        select_sem=int(input("Press 1 for 1 Semester \t Press 0 for exit:"))
        if select_sem==1:
            select_class=int(input("Press 1 for Group 15 \t Press 2 for Adding a Group \t Press 3 for Removing a Group\t Press 0 for exit:"))
            if select_class==1:
                att_excel_se=int(input("Press 1 for Save\t Press 2 for Choosing Another Date\t Press 3 for Dashboard\t Press 0 for exit: "))
                if att_excel_se==0:
                    exit()
                elif att_excel_se==1:
                    print("Saved")
        elif select_sem==0:
            exit()
        else:
            print("Type Valid Value")
    
    
    
    
    
    
    
    
    
    
    
    
else:
    exit()
    
    