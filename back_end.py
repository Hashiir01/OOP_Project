import sqlite3 as sql_db
import datetime

class DBManager:
    def __init__(self, filename:str, con=None, cur=None):
        if con is None:
            con = sql_db.connect(filename)
        if cur is None:
            cur = con.cursor()
        self.con = con
        self.cur = cur
        print('DBManager Initialized!!!')

    # screen function
    def all_match_schedules(self):
        query = '''
            SELECT match.team_names, match.date_time, stadium.stadium_name, stadium.location, match.match_id
            FROM match
            JOIN stadium ON match.stadium_id = stadium.stadium_id;
        '''
        self.cur.execute(query)
        data = self.cur.fetchall()
        out_str = ''
        for row in data:
            teams = row[0].split(',')
            out_str += teams[0]
            out_str += ' VS '
            out_str += teams[1]
            out_str += '--'
            out_str += row[2]
            out_str += '--'
            out_str += row[3]
            out_str += '--'
            out_str += row[1]
            out_str += '\tid = \t'
            out_str += str(row[-1])
            out_str += '\n'
        return out_str





    # basic functions
    def available_tickets(self, match_id:int):
        # avaiable tickets are those which are set to fan_id = -1
        query00 = '''
            select ticket_id from tickets
            where fan_id = -1 and match_id = ?
        '''
        self.cur.execute(query00, (match_id,))
        data = self.cur.fetchall()
        out_str = f'Avaiable ticket_ids for match_id = {match_id} are: \n'
        for row in data:
            out_str += f'id = {row[0]}\n'
        return out_str

    def ticket_validity(self, ticket_id:int):
        # a ticket is valid only if the fan_id is positive
        query00 = '''
            SELECT 1
            FROM tickets
            WHERE ticket_id = ? AND fan_id > 0
        '''
        self.cur.execute(query00, (ticket_id, ))
        data = self.cur.fetchall()
        if data:
            out_str = f'Congratulations! ticket is valid for id = {ticket_id}'
        else:
            out_str = f'Ticket is not valid with id = {ticket_id}! Please Buy a valid ticket'
        return out_str

    def fan_details(self, fan_id:int, cnic:str):
        if fan_id > 0:
            try:
                query00 = '''
                    select name, cnic, phone_number, email, payment_method from fan
                    where fan_id = ?
                '''
                self.cur.execute(query00, (fan_id, ))
                data = self.cur.fetchone()
                out_str = f'Details for fan_id = {fan_id}: \n'
                out_str += f'Name: {data[0]}\nCNIC: {data[1]}\nPhone Number: {data[2]}\nEmail: {data[3]}\nPayment Method: {data[4]}'
                return out_str
            except:
                return f'Error! fan not found!!!'
        elif cnic != '':
            try:
                query00 = '''
                    select fan_id, name, phone_number, email, payment_method from fan
                    where cnic = ?
                '''
                self.cur.execute(query00, (cnic, ))
                data = self.cur.fetchone()
                out_str = f'Details for cnic = {cnic}: \n'
                out_str += f'fan_id: {data[0]}\nName: {data[1]}\nPhone Number: {data[2]}\nEmail: {data[3]}\nPayment Method: {data[4]}'
                return out_str
            except:
                return f'Error! fan not found!!!'
        else:
            out_str = 'Please provide valid inputs!!!'
            return out_str

    def match_details(self, ticket_id:int, match_id:int):
        if ticket_id > 0:
            try:
                query00 = '''
                    SELECT match.team_names, match.date_time, stadium.stadium_name, stadium.location
                    FROM tickets
                    JOIN stadium ON tickets.stadium_id = stadium.stadium_id
                    JOIN match ON tickets.match_id = match.match_id  -- Adjust this line based on your actual schema
                    WHERE tickets.ticket_id = ?;
                '''
                self.cur.execute(query00, (ticket_id, ))
                data = self.cur.fetchone()
                teams = data[0].split(',')
                out_str = f'{teams[0]} VS {teams[1]}\n{data[2]} -- {data[3]}\nTime: {data[1]}'
                return out_str
            except:
                return f'Error! Match not found!!!'
        elif match_id > 0:
            try:
                query00 = '''
                    SELECT match.team_names, match.date_time, stadium.stadium_name, stadium.location
                    FROM match
                    JOIN stadium ON match.stadium_id = stadium.stadium_id
                    WHERE match.match_id = ?
                '''
                self.cur.execute(query00, (match_id, ))
                data = self.cur.fetchone()
                teams = data[0].split(',')
                out_str = f'{teams[0]} VS {teams[1]}\n{data[2]} -- {data[3]}\nTime: {data[1]}'
                return out_str
            except:
                return f'Error! Match not found!!!'
        else:
            out_str = 'Please provide valid inputs!!!'
            return out_str

    def purchase_history(self, fan_id:int, cnic:str):
        if fan_id > 0:
            try:
                query00 = '''
                    SELECT purchase_log.ticket_id, purchase_log.purchase_time, tickets.ticket_price, match.team_names, match.date_time
                    FROM purchase_log
                    JOIN tickets ON tickets.ticket_id = purchase_log.ticket_id
                    JOIN match ON tickets.match_id = match.match_id
                    JOIN fan ON tickets.fan_id = fan.fan_id
                    WHERE tickets.fan_id = ?;
                '''
                self.cur.execute(query00, (fan_id, ))
                data = self.cur.fetchall()
                if data:
                    out_str = ''
                    for row in data:
                        teams = row[3].split(',')
                        out_str += f'ID = {row[0]}\n{teams[0]} VS {teams[1]} AT:  {row[4]}\nEnclosure: \'{row[2]}\' Purchased AT: {row[1]}\n----------\n'
                else:
                    out_str = f'Error! purchase history not found!!!'
                return out_str
            except:
                return f'Error! purchase history not found!!!'
        elif cnic > 0:
            try:
                query00 = '''
                    SELECT purchase_log.ticket_id, purchase_log.purchase_time, tickets.ticket_price, match.team_names, match.date_time
                    FROM purchase_log
                    JOIN tickets ON tickets.ticket_id = purchase_log.ticket_id
                    JOIN match ON tickets.match_id = match.match_id
                    JOIN fan ON tickets.fan_id = fan.fan_id
                    WHERE fan.cnic = ?;
            '''
                self.cur.execute(query00, (cnic, ))
                data = self.cur.fetchall()
                if data:
                    out_str = ''
                    for row in data:
                        teams = row[3].split(',')
                        out_str += f'ID = {row[0]}\n{teams[0]} VS {teams[1]} AT:  {row[4]}\nEnclosure: \'{row[2]}\' Purchased AT: {row[1]}\n----------\n'
                else:
                    out_str = f'Error! purchase history not found!!!'
                return out_str
            except:
                return f'Error! purchase history not found!!!'
        else:
            out_str = 'Please provide valid inputs!!!'
            return out_str

    def stadium_details(self, stadium_id:int, ticket_id:int):
        if stadium_id > 0:
            try:
                query00 = '''
                    SELECT stadium_name, location, capacity
                    FROM stadium
                    WHERE stadium_id = ?
                '''
                self.cur.execute(query00, (stadium_id, ))
                data = self.cur.fetchone()
                if data:
                    out_str = f'ID: {stadium_id}\nStadium Name: {data[0]}\nLocation: {data[1]}\nCapacity: {data[-1]}'
                else:
                    out_str = f'Error! Stadium against ID = {stadium_id} not found!!!'
                return out_str
            except:
                out_str = f'Error! Stadium against ID = {stadium_id} not found!!!'
                return out_str
        elif ticket_id > 0:
            try:
                query00 = '''
                    SELECT stadium.stadium_name, stadium.location, stadium.capacity
                    FROM stadium
                    JOIN tickets ON tickets.stadium_id = stadium.stadium_id
                    WHERE tickets.ticket_id = ?;
            '''
                self.cur.execute(query00, (ticket_id, ))
                data = self.cur.fetchone()
                if data:
                    out_str = f'ID: {ticket_id}\nStadium Name: {data[0]}\nLocation: {data[1]}\nCapacity: {data[-1]}'
                else:
                    out_str = f'Error! Stadium against Ticket ID = {ticket_id} not found!!!'
                return out_str
            except:
                out_str = f'Error! S000tadium against Ticket ID = {ticket_id} not found!!!'
                return out_str
        else:
            out_str = 'Please provide valid inputs!!!'
            return out_str

    def stadium_capacity(self, stadium_id:int, ticket_id:int):
        if stadium_id > 0:
            try:
                query00 = '''
                    SELECT capacity
                    FROM stadium
                    WHERE stadium_id = ?
                '''
                self.cur.execute(query00, (stadium_id, ))
                data = self.cur.fetchone()
                if data:
                    out_str = f'ID: {stadium_id}\nCapacity: {data[-1]}'
                else:
                    out_str = f'Error! Stadium against ID = {stadium_id} not found!!!'
                return out_str
            except:
                out_str = f'Error! Stadium against ID = {stadium_id} not found!!!'
                return out_str
        elif ticket_id > 0:
            try:
                query00 = '''
                    SELECT stadium.capacity
                    FROM stadium
                    JOIN tickets ON tickets.stadium_id = stadium.stadium_id
                    WHERE tickets.ticket_id = ?;
            '''
                self.cur.execute(query00, (ticket_id, ))
                data = self.cur.fetchone()
                if data:
                    out_str = f'ID: {ticket_id}\nCapacity: {data[-1]}'
                else:
                    out_str = f'Error! Stadium against Ticket ID = {ticket_id} not found!!!'
                return out_str
            except:
                out_str = f'Error! S000tadium against Ticket ID = {ticket_id} not found!!!'
                return out_str
        else:
            out_str = 'Please provide valid inputs!!!'
            return out_str

    def update_auto(self):
        query = '''
            SELECT tickets.ticket_price
            FROM tickets
            JOIN purchase_log ON purchase_log.ticket_id = tickets.ticket_id
            WHERE purchase_log.refund_status = 0
        '''
        self.cur.execute(query)
        data = self.cur.fetchall()
        prices = {
            'Premium': 10000,
            'VIP': 8000,
            'First Class': 5000,
            'General': 2000,
        }
        total_revenue = 0
        for trow in data:
            total_revenue += prices[trow[0]]
        query0 = '''
            SELECT ticket_id
            FROM purchase_log
            WHERE refund_status = 1
        '''
        self.cur.execute(query0)
        data0 = self.cur.fetchall()
        data0 = [row[0] for row in data0]
        out_str = f'(Auto Updated after every\n5 seconds) \n\nTotal Revenue Generated: \n{total_revenue} Rs\nCount of Refunded Tickets:\n{len(data0)//2}'
        return out_str

    # advanced functions
    def create_new_fan_id(self):
        query = '''
            SELECT fan_id
            FROM fan
        '''
        self.cur.execute(query)
        data = self.cur.fetchall()
        data = [row[0] for row in data]
        return max(data) + 1

    def register_new_fan(self, name:str, cnic:str, phone: str, email:str, payment_method: str):
        if name and cnic and phone and email and payment_method:
            query = '''
                SELECT 1
                FROM fan
                WHERE cnic = ?
            '''
            self.cur.execute(query, (cnic,))
            chk = self.cur.fetchone()
            if not chk:
                query00 = '''
                    INSERT INTO fan (fan_id, name, cnic, phone_number, email, payment_method)
                    VALUES (?, ?, ?, ?, ?, ?);
                '''
                myfanid = self.create_new_fan_id()
                self.cur.execute(query00, (myfanid, name, cnic, phone, email, payment_method))
                self.con.commit()
                return f'fan added successfully\nfan_id is generated automatically: {myfanid}'
            else:
                return f'Fan already exists!!!'
        else:
            return f'Please provide inputs in all data fields!!!'


    def create_new_log_id(self):
        query = '''
            SELECT log_id
            FROM purchase_log
        '''
        self.cur.execute(query)
        data = self.cur.fetchall()
        data = [row[0] for row in data]
        return max(data) + 1

    def refund_payment(self, fan_id:int, ticket_id:int, payment_method:str):
        try:
            query0 = '''
                SELECT 1
                FROM purchase_log
                WHERE ticket_id = ? AND refund_status = 0;
            '''
            self.cur.execute(query0, (ticket_id,))
            chk = self.cur.fetchone()
            if chk:
                query00 = '''
                    UPDATE tickets
                    SET fan_id = -1
                    FROM purchase_log
                    WHERE tickets.ticket_id = purchase_log.ticket_id AND purchase_log.ticket_id = ?;
                '''
                self.cur.execute(query00, (ticket_id,))
                query000 = '''
                    INSERT INTO purchase_log(log_id, ticket_id, purchase_time, payment_method, refund_status)
                    VALUES(?,?,?,?,?);
                '''
                self.cur.execute(query000, (self.create_new_log_id(), ticket_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),payment_method,1))
                query0000 = '''
                    UPDATE purchase_log
                    SET refund_status = 1
                    WHERE ticket_id = ?
                '''
                self.cur.execute(query0000, (ticket_id,))
                self.con.commit()
                return f'Refund Successful against ticket_id = {ticket_id}, fan_id = {fan_id}'
            else:
                return f'Error!!! Purchase against Ticket id = {ticket_id} not found'
        except:
            return f'Unexpected Error Occurred!!!'


    def get_new_ticket_id(self, fan_id):
        query = '''
			SELECT ticket_id
			FROM tickets
			WHERE fan_id = -1
			LIMIT 1;
        '''
        self.cur.execute(query)
        data = self.cur.fetchone()
        query0 = '''
            UPDATE tickets
            SET fan_id = ?
            WHERE ticket_id = ?
        '''
        self.cur.execute(query0, (fan_id, data[0]))
        return data[0]

    def purchase_ticket(self, match_id: int, enclosure: str, name:str, cnic:str, phone: str, email:str, payment_method: str):
        if match_id and enclosure and name and cnic and phone and email and payment_method:
            query = '''
                SELECT 1
                FROM fan
                WHERE cnic = ?
            '''
            self.cur.execute(query, (cnic,))
            chk = self.cur.fetchone()
            if not chk:
                query00 = '''
                    INSERT INTO fan (fan_id, name, cnic, phone_number, email, payment_method)
                    VALUES (?, ?, ?, ?, ?, ?);
                '''
                myfanid = self.create_new_fan_id()
                self.cur.execute(query00, (myfanid, name, cnic, phone, email, payment_method))
            else:
                query0000 = '''
                    SELECT fan_id
                    FROM fan
                    WHERE cnic = ?
                '''
                self.cur.execute(query0000, (cnic,))
                dat10 = self.cur.fetchone()
                myfanid = dat10[0]
            query000 = '''
                INSERT INTO purchase_log(log_id, ticket_id, purchase_time, payment_method, refund_status)
                VALUES(?,?,?,?,?);
            '''
            my_ticket_id = self.get_new_ticket_id(myfanid)
            self.cur.execute(query000, (self.create_new_log_id(), my_ticket_id, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),payment_method,0))
            self.con.commit()
            last_query = '''
                    SELECT match.team_names, match.date_time, stadium.stadium_name, stadium.location
                    FROM tickets
                    JOIN stadium ON tickets.stadium_id = stadium.stadium_id
                    JOIN match ON tickets.match_id = match.match_id  -- Adjust this line based on your actual schema
                    WHERE tickets.ticket_id = ?;
                '''
            self.cur.execute(last_query, (my_ticket_id, ))
            data = self.cur.fetchone()
            teams = data[0].split(',')
            out_str = f'Purchase Successful!!\nYour ticket_id is {my_ticket_id}\n\nDetails:\n'
            out_str += f'{teams[0]} VS {teams[1]}\n{data[2]} -- {data[3]}\nTime: {data[1]}'
            return out_str
        else:
            return f'Please provide inputs in all datafields!!!'

def main():
    filename = "database.db"
    layer = DBManager(filename)
    return layer
    # print(layer.all_match_schedules())
    # print(layer.available_tickets(10))
    # print(layer.ticket_validity(40))
    # print(layer.ticket_validity(23))
    # print(layer.fan_details(1, -1))
    # print(layer.match_details(1,1))
    # print(layer.purchase_history(0, 1234567023))
    # print(layer.stadium_details(0, 1))
    # print(layer.register_new_fan('Subhan Ali', '3520207870000', '03084072295', 'subhanali1212w@gmail.com', 'DEBIT CARD'))
    # print(layer.create_new_fan_id())
    # print(layer.refund_payment(1, 1, 'BANK TRANSFER'))
    # print(layer.purchase_ticket(1, 'VIP', 'Subhan Ali', '3520207870453', '03084072295', 'subhanali1212w@gmail.com', 'DEBIT CARD'))
if __name__ == '__main__':
    main()