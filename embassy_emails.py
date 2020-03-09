import yagmail

user = input("Please enter email: ")
password = input("Please enter password: ")
subject = "Inquiry About Your Nation's Flag"

yag = yagmail.SMTP(user=user, password=password)

nation_file = open("EMBASSIES.txt", "r") #each line is composed: country,email,greeting

for line in nation_file.readlines():
    line_list = line.split(",")
    country, embassy_email, greeting = line_list[0], line_list[1], line_list[2]

    contents = [
        "Dear Representatives of " + country + ",",
        "\n",
        greeting + " I hope this message finds you well. My name is [name] and I am an avid collector of flags. Over"
        " some years, I have amassed a large collection, however I do not have the flag belonging to your beautiful"
        " nation, " + country + ". While I am determined to one day visit and experience your country, I was hoping"
        " that, in the meantime, I could trouble you to send me your nation's flag (large or small) so that I may add"
        " it to my collection. That is, of course, if you are able.",
        "\n",
        "My address is as follows:",
        "[full name]",
        "[street]",
        "[city, state, zip]",
        "\n",
        "Sincerely Yours,",
        "\n",
        "[full name]"
    ]

    print("Sending email to " + country + "...")
    yag.send(embassy_email, subject, contents)

nation_file.close()