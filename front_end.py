# creted by subhan ali - bsdsf22m030, 24, 26, 46, 36


from tkinter import *
from tkinter import ttk
import back_end
root = Tk()
root.title("Tickets")
# main topic
topic = Label(root, text="PSL Ticket Management System", font=('Helvetica', 18))
topic.grid(row=0, column=0, padx=10, sticky=W, columnspan=3)

# creating label frames
# frame two
f_two = LabelFrame(root, text="SCREEN / FRAME 2", borderwidth=1, padx=5, pady=5, width=1090, height=300)
f_two.grid_propagate(FALSE)
f_two.grid(row=1, column=0, sticky=W, columnspan=3)
# frame one
f_one = LabelFrame(root, text="BASIC FUNCTIONS", borderwidth=1, width=218, height=250)
f_one.grid_propagate(FALSE)
f_one.grid(row=2, column=0, padx=5, pady=5, sticky=W)
# frame advamced
f_three = LabelFrame(root, text="ADVANCED FUNCTIONS", borderwidth=1, width=200, height=250)
f_three.grid_propagate(FALSE)
f_three.grid(row=2, column=2, padx=5, pady=5, sticky=W)


# labelframe for tabs
label_frame_tab = LabelFrame(root, text="Tabs", borderwidth=1, width=654, height=250)
label_frame_tab.grid_propagate(FALSE)
label_frame_tab.grid(row=2, column=1, sticky=W)

# tabs
main_tab_container = ttk.Notebook(label_frame_tab)
main_tab_container.grid_propagate(FALSE)
main_tab_container.grid(sticky=W)

def resolve_curr_tab():
    tot_tabs = main_tab_container.winfo_children()
    print('total tabs = ', len(tot_tabs))
    new_curr = len(tot_tabs) - 1
    s = ttk.Style()
    s.theme_use('default')
    s.configure('TNotebook.Tab', background="#A8B3FD")
    try:
        main_tab_container.select(new_curr)
    except:
        pass







def proceed_match_id():
    out_str = ''
    inst = back_end.main()
    if t1.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        out_str = inst.available_tickets(int(t1.get()))
    t1.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)


def add_tab0():
    # tabs frame
    frame_tab_0 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_0.grid_propagate(FALSE)
    frame_tab_0.grid(sticky = W)

    # label
    l3 = Label(frame_tab_0, text='Enter Match ID: ')
    l3.grid(row=0, column=0, sticky=W)
    # entry
    global t1
    t1 = Entry(frame_tab_0, width=10, borderwidth=2)
    t1.grid(row=0, column=1, sticky=W)

    # submit but
    sub_but = Button(frame_tab_0, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=proceed_match_id)
    sub_but.grid(row=1, column=1, sticky=E, rowspan=2)

    # adding tabs
    main_tab_container.add(frame_tab_0, text="Tickets")
    resolve_curr_tab()




def validity_chk():
    out_str = ''
    inst = back_end.main()
    if t2.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        out_str = inst.ticket_validity(int(t2.get()))
    t2.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)



def add_tab1():
    # tabs frame
    frame_tab_1 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_1.grid_propagate(FALSE)
    frame_tab_1.grid(sticky=W)

    # label
    l3 = Label(frame_tab_1, text='Enter Ticket ID: ')
    l3.grid(row=0, column=0, sticky=W)
    # entry
    global t2
    t2 = Entry(frame_tab_1, width=10, borderwidth=2)
    t2.grid(row=0, column=1, sticky=W)

    # submit but
    sub_but = Button(frame_tab_1, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=validity_chk)
    sub_but.grid(row=1, column=1, sticky=E, rowspan=2)

    # adding tabs
    main_tab_container.add(frame_tab_1, text="Ticket Validity")
    resolve_curr_tab()



def get_fan_details():
    out_str = ''
    inst = back_end.main()
    if t1_fan_id.get() == '' and t1_cnic.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        if t1_fan_id.get() == '' and t1_cnic.get() != '':
            out_str = inst.fan_details(-1, int(t1_cnic.get()))
        elif t1_fan_id.get() != '' and t1_cnic.get() == '':
            out_str = inst.fan_details(int(t1_fan_id.get()), -1)
        elif t1_fan_id.get() != '' and t1_cnic.get() != '':
            out_str = inst.fan_details(int(t1_fan_id.get()), int(t1_cnic.get()))
        else:
            out_str = f'An unexpected error occurred!!'
        # return out_str
    t1_fan_id.delete(0, END)
    t1_cnic.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)



def add_tab2():
    # tabs frame
    frame_tab_2 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_2.grid_propagate(FALSE)
    frame_tab_2.grid(sticky=W)

    l0 = Label(frame_tab_2, text='Please fill one or more options below: ')
    l0.grid(row=0, column=0, sticky=W, columnspan=2)
    
    # label
    l3 = Label(frame_tab_2, text='Enter Fan ID: ')
    l3.grid(row=1, column=0, sticky=W)
    # entry
    global t1_fan_id
    t1_fan_id = Entry(frame_tab_2, width=10, borderwidth=2)
    t1_fan_id.grid(row=1, column=1, sticky=W)

    # label
    l4 = Label(frame_tab_2, text='Enter Fan CNIC: ')
    l4.grid(row=2, column=0, sticky=W)
    # entry
    global t1_cnic
    t1_cnic = Entry(frame_tab_2, width=10, borderwidth=2)
    t1_cnic.grid(row=2, column=1, sticky=W)
    
    # submit but
    sub_but = Button(frame_tab_2, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=get_fan_details)
    sub_but.grid(row=3, column=1, sticky=E, rowspan=2)


    # adding tabs
    main_tab_container.add(frame_tab_2, text="Fan Details")
    resolve_curr_tab()


def get_match_details():
    out_str = ''
    inst = back_end.main()
    if t1_ticket_id.get() == '' and t1_match_id.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        if t1_ticket_id.get() == '' and t1_match_id.get() != '':
            out_str = inst.match_details(-1, int(t1_match_id.get()))
        elif t1_ticket_id.get() != '' and t1_match_id.get() == '':
            out_str = inst.match_details(int(t1_ticket_id.get()), -1)
        elif t1_ticket_id.get() != '' and t1_match_id.get() != '':
            out_str = inst.match_details(int(t1_ticket_id.get()), int(t1_match_id.get()))
        else:
            out_str = f'An unexpected error occurred!!'
        # return out_str
    t1_ticket_id.delete(0, END)
    t1_match_id.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)


def add_tab3():
    # tabs frame
    frame_tab_3 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_3.grid_propagate(FALSE)
    frame_tab_3.grid(sticky=W)

    l0 = Label(frame_tab_3, text='Please fill one or more options below: ')
    l0.grid(row=0, column=0, sticky=W, columnspan=2)

    # label
    l3 = Label(frame_tab_3, text='Enter Ticket ID: ')
    l3.grid(row=1, column=0, sticky=W)
    # entry
    global t1_ticket_id
    t1_ticket_id = Entry(frame_tab_3, width=10, borderwidth=2)
    t1_ticket_id.grid(row=1, column=1, sticky=W)

    # label
    l4 = Label(frame_tab_3, text='Enter Match ID: ')
    l4.grid(row=2, column=0, sticky=W)
    # entry
    global t1_match_id
    t1_match_id = Entry(frame_tab_3, width=10, borderwidth=2)
    t1_match_id.grid(row=2, column=1, sticky=W)
    
    # submit but
    sub_but = Button(frame_tab_3, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=get_match_details)
    sub_but.grid(row=3, column=1, sticky=E, rowspan=2)

    # adding tabs
    main_tab_container.add(frame_tab_3, text="Match Details")
    resolve_curr_tab()


def get_purchase_history():
    out_str = ''
    inst = back_end.main()
    if t1_purchase_history0.get() == '' and t1_purchase_history1.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        if t1_purchase_history0.get() == '' and t1_purchase_history1.get() != '':
            out_str = inst.purchase_history(-1, int(t1_purchase_history1.get()))
        elif t1_purchase_history0.get() != '' and t1_purchase_history1.get() == '':
            out_str = inst.purchase_history(int(t1_purchase_history0.get()), -1)
        elif t1_purchase_history0.get() != '' and t1_purchase_history1.get() != '':
            out_str = inst.purchase_history(int(t1_purchase_history0.get()), int(t1_purchase_history1.get()))
        else:
            out_str = f'An unexpected error occurred!!'
        # return out_str
    t1_purchase_history0.delete(0, END)
    t1_purchase_history1.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)
    
def add_tab4():
    # tabs frame
    frame_tab_4 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_4.grid_propagate(FALSE)
    frame_tab_4.grid(sticky=W)

    l0 = Label(frame_tab_4, text='Please fill one or more options below: ')
    l0.grid(row=0, column=0, sticky=W, columnspan=2)
    
    # label
    l3 = Label(frame_tab_4, text='Enter Fan ID: ')
    l3.grid(row=1, column=0, sticky=W)
    # entry
    global t1_purchase_history0
    t1_purchase_history0 = Entry(frame_tab_4, width=10, borderwidth=2)
    t1_purchase_history0.grid(row=1, column=1, sticky=W)

    # label
    l4 = Label(frame_tab_4, text='Enter Fan CNIC: ')
    l4.grid(row=2, column=0, sticky=W)
    # entry
    global t1_purchase_history1
    t1_purchase_history1 = Entry(frame_tab_4, width=10, borderwidth=2)
    t1_purchase_history1.grid(row=2, column=1, sticky=W)
    
    # submit but
    sub_but = Button(frame_tab_4, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=get_purchase_history)
    sub_but.grid(row=3, column=1, sticky=E, rowspan=2)

    # adding tabs
    main_tab_container.add(frame_tab_4, text="Purchase History")
    resolve_curr_tab()


def get_stadium_details():
    out_str = ''
    inst = back_end.main()
    if t1_stadium_id.get() == '' and t1_ticket_id0.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        if t1_stadium_id.get() == '' and t1_ticket_id0.get() != '':
            out_str = inst.stadium_details(-1, int(t1_ticket_id0.get()))
        elif t1_stadium_id.get() != '' and t1_ticket_id0.get() == '':
            out_str = inst.stadium_details(int(t1_stadium_id.get()), -1)
        elif t1_stadium_id.get() != '' and t1_ticket_id0.get() != '':
            out_str = inst.stadium_details(int(t1_stadium_id.get()), int(t1_ticket_id0.get()))
        else:
            out_str = f'An unexpected error occurred!!'
        # return out_str
    t1_stadium_id.delete(0, END)
    t1_ticket_id0.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)


def add_tab5():
    # tabs frame
    frame_tab_5 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_5.grid_propagate(FALSE)
    frame_tab_5.grid(sticky=W)

    l0 = Label(frame_tab_5, text='Please fill one or more options below: ')
    l0.grid(row=0, column=0, sticky=W, columnspan=2)
    
    # label
    l3 = Label(frame_tab_5, text='Enter Stadium ID: ')
    l3.grid(row=1, column=0, sticky=W)
    # entry
    global t1_stadium_id
    t1_stadium_id = Entry(frame_tab_5, width=10, borderwidth=2)
    t1_stadium_id.grid(row=1, column=1, sticky=W)

    # label
    l4 = Label(frame_tab_5, text='Enter Ticket ID: ')
    l4.grid(row=2, column=0, sticky=W)
    # entry
    global t1_ticket_id0
    t1_ticket_id0 = Entry(frame_tab_5, width=10, borderwidth=2)
    t1_ticket_id0.grid(row=2, column=1, sticky=W)
    
    # submit but
    sub_but = Button(frame_tab_5, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=get_stadium_details)
    sub_but.grid(row=3, column=1, sticky=E, rowspan=2)

    # adding tabs
    main_tab_container.add(frame_tab_5, text="Stadium Details")
    resolve_curr_tab()


def get_stadium_capacity():
    out_str = ''
    inst = back_end.main()
    if t1_stadium_id0.get() == '' and t1_ticket_id00.get() == '':
        out_str = 'Please enter input in data fields before proceeding!!!'
    else:
        if t1_stadium_id0.get() == '' and t1_ticket_id00.get() != '':
            out_str = inst.stadium_capacity(-1, int(t1_ticket_id00.get()))
        elif t1_stadium_id0.get() != '' and t1_ticket_id00.get() == '':
            out_str = inst.stadium_capacity(int(t1_stadium_id0.get()), -1)
        elif t1_stadium_id0.get() != '' and t1_ticket_id00.get() != '':
            out_str = inst.stadium_capacity(int(t1_stadium_id0.get()), int(t1_ticket_id00.get()))
        else:
            out_str = f'An unexpected error occurred!!'
    t1_stadium_id0.delete(0, END)
    t1_ticket_id00.delete(0, END)
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)

def add_tab6():
    # tabs frame
    frame_tab_6 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_6.grid_propagate(FALSE)
    frame_tab_6.grid(sticky=W)

    l0 = Label(frame_tab_6, text='Please fill one or more options below: ')
    l0.grid(row=0, column=0, sticky=W, columnspan=2)
    
    # label
    l3 = Label(frame_tab_6, text='Enter Stadium ID: ')
    l3.grid(row=1, column=0, sticky=W)
    # entry
    global t1_stadium_id0
    t1_stadium_id0 = Entry(frame_tab_6, width=10, borderwidth=2)
    t1_stadium_id0.grid(row=1, column=1, sticky=W)

    # label
    l4 = Label(frame_tab_6, text='Enter Ticket ID: ')
    l4.grid(row=2, column=0, sticky=W)
    # entry
    global t1_ticket_id00
    t1_ticket_id00 = Entry(frame_tab_6, width=10, borderwidth=2)
    t1_ticket_id00.grid(row=2, column=1, sticky=W)
    
    # submit but
    sub_but = Button(frame_tab_6, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=get_stadium_capacity)
    sub_but.grid(row=3, column=1, sticky=E, rowspan=2)

    main_tab_container.add(frame_tab_6, text="Stadium Capacity")
    resolve_curr_tab()

def purchase_func_backend():
    if t0_name0.get() and t1_cnic00.get() and t2_phone0.get() and t3_email0.get():
        inst = back_end.main()
        try:
            enc = opt1_var.get()
            enc = enc.split(',')
            out_str = inst.purchase_ticket(opt0_var.get()[-1], enc[0], t0_name0.get(), t1_cnic00.get(), t2_phone0.get(), t3_email0.get(), opt2_var00.get())
            if screen_frame.get("1.0", "end-1c") != "":
                screen_frame.delete("1.0", END)
            screen_frame.insert("1.0", out_str)
        except:
            out_str = 'Unexpected Error Occurred00000000!!!'
            if screen_frame.get("1.0", "end-1c") != "":
                screen_frame.delete("1.0", END)
            screen_frame.insert("1.0", out_str)
    else:
        out_str = 'Please provide complete inputs in datafields!!!'
        if screen_frame.get("1.0", "end-1c") != "":
            screen_frame.delete("1.0", END)
        screen_frame.insert("1.0", out_str)
    t0_name0.delete(0, END)
    t1_cnic00.delete(0, END)
    t2_phone0.delete(0, END)
    t3_email0.delete(0, END)



def add_tab_pur_ticket():
    # tabs frame
    frame_tab_7 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_7.grid_propagate(FALSE)
    frame_tab_7.grid(sticky=W)
    # label
    l0 = Label(frame_tab_7, text='Choose Match_id of Your Choice: ')
    l0.grid(row=0, column=0, sticky=W)
    # options
    options = ['Match 1', 'Match 2', 'Match 3', 'Match 4', 'Match 5', 'Match 6', 'Match 7', 'Match 8', 'Match 9', 'Match 10']
    global opt0_var
    opt0_var = StringVar(value=options[0])
    opt0 = OptionMenu(frame_tab_7, opt0_var, *options)
    opt0.grid(row=0, column=1, sticky=W)

    # label
    l1 = Label(frame_tab_7, text='Choose Ticket Enclosure: ')
    l1.grid(row=1, column=0, sticky=W)
    # options
    tik_options = ['Premium, 10000', 'VIP, 8000', 'First Class, 5000', 'General, 2000']
    global opt1_var
    opt1_var = StringVar(value=tik_options[0])
    opt1 = OptionMenu(frame_tab_7, opt1_var, *tik_options)
    opt1.grid(row=1, column=1, sticky=W)

    # label
    l2 = Label(frame_tab_7, text='Seat will be selected Automatically!!!')
    l2.grid(row=2, column=0, sticky=W)

    # label
    l3 = Label(frame_tab_7, text='Enter Personal Details: \nFan will be created automatically if not exists!!!')
    l3.grid(row=4, column=0, sticky=W, columnspan=2)

    # label
    l3_name = Label(frame_tab_7, text='Name: ')
    l3_name.grid(row=5, column=0, sticky=W)
    # entry
    global t0_name0
    t0_name0 = Entry(frame_tab_7, width=10, borderwidth=2)
    t0_name0.grid(row=5, column=1, sticky=W)

    # label
    l3_cnic = Label(frame_tab_7, text='CNIC: ')
    l3_cnic.grid(row=6, column=0, sticky=W)
    # entry
    global t1_cnic00
    t1_cnic00 = Entry(frame_tab_7, width=10, borderwidth=2)
    t1_cnic00.grid(row=6, column=1, sticky=W)

    # label
    l3_phone = Label(frame_tab_7, text='Phone: ')
    l3_phone.grid(row=7, column=0, sticky=W)
    # entry
    global t2_phone0
    t2_phone0 = Entry(frame_tab_7, width=10, borderwidth=2)
    t2_phone0.grid(row=7, column=1, sticky=W)

    # label
    l3_email = Label(frame_tab_7, text='Email: ')
    l3_email.grid(row=1, column=2, sticky=W)
    # entry
    global t3_email0
    t3_email0 = Entry(frame_tab_7, width=10, borderwidth=2)
    t3_email0.grid(row=1, column=3, sticky=W)


    # label
    l4 = Label(frame_tab_7, text='-------- Payment Details --------')
    l4.grid(row=0, column=2, sticky=W, columnspan=2)
    l4_pay = Label(frame_tab_7, text='Select Payment Method: ')
    l4_pay.grid(row=2, column=2, sticky=W)
    # options
    pay_options = ['BANK TRANSFER', 'DEBIT CARD', 'JAZZCASH']
    global opt2_var00
    opt2_var00 = StringVar(value=pay_options[0])
    opt2 = OptionMenu(frame_tab_7, opt2_var00, *pay_options)
    opt2.grid(row=2, column=3, sticky=W)
    # submit but
    sub_but = Button(frame_tab_7, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=purchase_func_backend)
    sub_but.grid(row=3, column=3, sticky=E, rowspan=2)

    main_tab_container.add(frame_tab_7, text="Purchase Ticket")
    resolve_curr_tab()


def register_new_fan_backend():
    inst = back_end.main()
    try:
        out_str = inst.register_new_fan(t0_name.get(), t1_cnic0.get(), t2_phone.get(), t3_email.get(), opt2_var.get())
        t0_name.delete(0, END)
        t1_cnic0.delete(0, END)
        t2_phone.delete(0, END)
        t3_email.delete(0, END)
        if screen_frame.get("1.0", "end-1c") != "":
            screen_frame.delete("1.0", END)
        screen_frame.insert("1.0", out_str)
    except:
        out_str = 'Unexpected Error Occurred!!!'
        if screen_frame.get("1.0", "end-1c") != "":
            screen_frame.delete("1.0", END)
        screen_frame.insert("1.0", out_str)


def add_tab_new_fan():
    # tabs frame
    frame_tab_8 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_8.grid_propagate(FALSE)
    frame_tab_8.grid(sticky=W)

    # label
    l3 = Label(frame_tab_8, text='Enter Personal Details: ')
    l3.grid(row=0, column=0, sticky=W, columnspan=2)

    # label
    l3_name = Label(frame_tab_8, text='Name: ')
    l3_name.grid(row=1, column=0, sticky=W)
    # entry
    global t0_name
    t0_name = Entry(frame_tab_8, width=10, borderwidth=2)
    t0_name.grid(row=1, column=1, sticky=W)

    # label
    l3_cnic = Label(frame_tab_8, text='CNIC: ')
    l3_cnic.grid(row=2, column=0, sticky=W)
    # entry
    global t1_cnic0
    t1_cnic0 = Entry(frame_tab_8, width=10, borderwidth=2)
    t1_cnic0.grid(row=2, column=1, sticky=W)

    # label
    l3_phone = Label(frame_tab_8, text='Phone: ')
    l3_phone.grid(row=3, column=0, sticky=W)
    # entry
    global t2_phone
    t2_phone = Entry(frame_tab_8, width=10, borderwidth=2)
    t2_phone.grid(row=3, column=1, sticky=W)

    # label
    l3_email = Label(frame_tab_8, text='Email: ')
    l3_email.grid(row=4, column=0, sticky=W)
    # entry
    global t3_email
    t3_email = Entry(frame_tab_8, width=10, borderwidth=2)
    t3_email.grid(row=4, column=1, sticky=W)


    # label
    l4 = Label(frame_tab_8, text='-------- Payment Details --------')
    l4.grid(row=0, column=2, sticky=W, columnspan=2)
    l4_pay = Label(frame_tab_8, text='Select Payment Method: ')
    l4_pay.grid(row=2, column=2, sticky=W)
    # options
    pay_options = ['BANK TRANSFER', 'DEBIT CARD', 'JAZZCASH']
    global opt2_var
    opt2_var = StringVar(value=pay_options[0])
    opt2 = OptionMenu(frame_tab_8, opt2_var, *pay_options)
    opt2.grid(row=2, column=3, sticky=W)
    # submit but
    sub_but = Button(frame_tab_8, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=register_new_fan_backend)
    sub_but.grid(row=3, column=3, sticky=E, rowspan=2)

    main_tab_container.add(frame_tab_8, text="New Fan")
    resolve_curr_tab()


def refund_func():
    if t0_fan_id.get() and t1_ticket_id010.get():
        inst = back_end.main()
        try:
            out_str = inst.refund_payment(t0_fan_id.get(), t1_ticket_id010.get(), opt2_var0.get())
            t1_ticket_id010.delete(0, END)
            if screen_frame.get("1.0", "end-1c") != "":
                screen_frame.delete("1.0", END)
            screen_frame.insert("1.0", out_str)
        except:
            out_str = 'Unexpected Error Occurred!!!'
            if screen_frame.get("1.0", "end-1c") != "":
                screen_frame.delete("1.0", END)
            screen_frame.insert("1.0", out_str)
    else:
        out_str = 'Please provide complete inputs in datafields!!!'
        if screen_frame.get("1.0", "end-1c") != "":
            screen_frame.delete("1.0", END)
        screen_frame.insert("1.0", out_str)
    t0_fan_id.delete(0, END)
    t1_ticket_id010.delete(0, END)


def add_tab_refund_ticket():
    # tabs frame
    frame_tab_9 = LabelFrame(main_tab_container, width=652, height=205)
    frame_tab_9.grid_propagate(FALSE)
    frame_tab_9.grid(sticky=W)

    # label
    l3 = Label(frame_tab_9, text='Enter FAN ID: ')
    l3.grid(row=0, column=0, sticky=W)
    # entry
    global t0_fan_id
    t0_fan_id = Entry(frame_tab_9, width=10, borderwidth=2)
    t0_fan_id.grid(row=0, column=1, sticky=W)

    # label
    l4 = Label(frame_tab_9, text='Enter Ticket ID: ')
    l4.grid(row=1, column=0, sticky=W)
    # entry
    global t1_ticket_id010
    t1_ticket_id010 = Entry(frame_tab_9, width=10, borderwidth=2)
    t1_ticket_id010.grid(row=1, column=1, sticky=W)

    l4_pay = Label(frame_tab_9, text='Select Refund Method: ')
    l4_pay.grid(row=2, column=2, sticky=W)
    # options
    pay_options = ['BANK TRANSFER', 'DEBIT CARD', 'JAZZCASH']
    global opt2_var0
    opt2_var0 = StringVar(value=pay_options[0])
    opt2 = OptionMenu(frame_tab_9, opt2_var0, *pay_options)
    opt2.grid(row=2, column=3, sticky=W)

    # submit but
    sub_but = Button(frame_tab_9, text="Submit", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=refund_func)
    sub_but.grid(row=3, column=3, sticky=E, rowspan=2)

    main_tab_container.add(frame_tab_9, text="Refund")
    resolve_curr_tab()



def all_match_schedules():
    inst = back_end.main()
    out_str = inst.all_match_schedules()
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)


def clear_scr():
    out_str = 'No text to display at the moment...'
    if screen_frame.get("1.0", "end-1c") != "":
        screen_frame.delete("1.0", END)
    screen_frame.insert("1.0", out_str)


# frame = screen / frame 2
screen_frame = Text(f_two, height=14, width=100)
screen_frame.grid(row=0, column=0)
screen_frame.insert("1.0", "No text to display at the moment...")
# screen separator
sep = ttk.Separator(f_two, orient='horizontal')
sep.grid(row=1, column=0, sticky=W+E, padx=0, pady=5)
# basic buttons
basic_button_0 = Button(f_two, text="Show Match Schedules", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), command=all_match_schedules)
basic_button_0.grid(row=2, column=0, sticky=W)
basic_button_1 = Button(f_two, text="Clear Screen", padx=20, pady= 0, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=clear_scr)
basic_button_1.grid(row=2, column=0, sticky=E)

def update_auto():
    f_two.after(5000, update_auto)
    inst = back_end.main()
    new_text = inst.update_auto()
    screen_frame_2.delete(1.0, END)
    screen_frame_2.insert(END, new_text)

def show_initial_text():
    screen_frame_2.insert("1.0", "No text to display at the \nmoment...")
    f_two.after(5000, update_auto)


# screen 2
screen_frame_2 = Text(f_two, height=18, width=30, bg='#ECECEC')
screen_frame_2.grid(row=0, column=1, padx=15, rowspan=6)
show_initial_text()




# frame = frame 1
# buy ticket<tab>         register new fan<tab>   get check ticket validity
# Get fan details         get match details           get purchase history
# refund process<tab>     get stadium details         get stadium capacity

# basic functions
avail_ticket_button = Button(f_one, text="Available Tickets", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab0)
avail_ticket_button.grid(row=0, column=1, sticky=W+E)
validity_ticket_button = Button(f_one, text="Ticket Validity", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab1)
validity_ticket_button.grid(row=1, column=1, sticky=W+E)
fan_details_button = Button(f_one, text="Fan Details", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab2)
fan_details_button.grid(row=2, column=1, sticky=W+E)
match_details_button = Button(f_one, text="Match Details", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab3)
match_details_button.grid(row=3, column=1, sticky=W+E)
history_button = Button(f_one, text="Purchase History", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab4)
history_button.grid(row=4, column=1, sticky=W+E)
stadium_details_button = Button(f_one, text="Stadium Details", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab5)
stadium_details_button.grid(row=5, column=1, sticky=W+E)
stadium_capacity_button = Button(f_one, text="Stadium Capacity", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab6)
stadium_capacity_button.grid(row=6, column=1, sticky=W+E)


# advanced functions
purchase_ticket_button = Button(f_three, text="Purchase Ticket", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab_pur_ticket)
purchase_ticket_button.grid(row=0, column=1, sticky=W+E)
reg_new_fan_button = Button(f_three, text="Register New Fan", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab_new_fan)
reg_new_fan_button.grid(row=1, column=1, sticky=W+E)
refund_button = Button(f_three, text="Refund Ticket", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), command=add_tab_refund_ticket)
refund_button.grid(row=2, column=1, sticky=W+E)

sepa = ttk.Separator(f_three, orient='horizontal')
sepa.grid(row=3, column=1, sticky=W+E, padx=10, pady=10)


def hide_one_tab():
    main_tab_container.forget("current")

def hide_all_tabs():
    while True:
        try:
            hide_one_tab()
        except:
            break

close_current_button = Button(f_three, text="Close Current Tab> X", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=hide_one_tab)
close_current_button.grid(row=4, column=1, sticky=W+E)
close_all_button = Button(f_three, text="Close All Tabs> O", padx=30, pady= 2, borderwidth=3, font=('sans-serif', 10), bg='#5A8AFF', fg='#ffffff', command=hide_all_tabs)
close_all_button.grid(row=5, column=1, sticky=W+E)


root.resizable(0, 0)
root.geometry("1100x600")
root.mainloop()