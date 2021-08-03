import pandas as pd
import datetime
import smtplib
import os

os.chdir(r"C:\Users\Intel\PycharmProjects\RP")


# Enter your authentication details
GMAIL_ID = ''
GMAIL_PSWD = ''


def sendEmail(to, sub, msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__ == "__main__":
    df = pd.read_excel("files/bday data.xlsx")
    # print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    # print(today)
    # print(type(today))
    yearNow = datetime.datetime.now().strftime("%Y")
    writeInd = []
    for index, item in df.iterrows():
        # print(index, item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'], "Happy Birthday", item['Message'])
            writeInd.append(index)

    # print(writeInd)
    if not writeInd:
        print("Today is either no one's birthday or those who had birthday today have been wished")
    else:
        for i in writeInd:
            yr = df.loc[i, 'Year']
            df.loc[i, 'Year'] = str(yr) + ', ' + str(yearNow)
            # print(df.loc[i, 'Year'])

    # print(df)
    df.to_excel('files/bday data.xlsx', index=False)
