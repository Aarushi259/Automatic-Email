import csv
from string import Template
import Conf

Email = Conf.Email
Passowrd = Conf.Passowrd


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def read_simple(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        return template_file_content


with open('Some.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    emails = []
    Names = []
    School_names = []
    Mode_of_transport = []

    for line in csv_reader:
        emails.append(str(line[0]))
        first_name = line[1].split(" ", 1)[0]
        Names.append(first_name)
        School_names.append(line[2])
        Mode_of_transport.append(line[3])

i = 0
message_template = read_template('message.txt')
subject_template = read_template('subject.txt')
size = len(emails)
subject = []
msg = []

while i < size:
    subject.append(subject_template.substitute(SCHOOL=School_names[i], BIKES=Mode_of_transport[i]))
    msg.append(message_template.substitute(PERSON_NAME=Names[i], BIKES=Mode_of_transport[i]))
    i += 1