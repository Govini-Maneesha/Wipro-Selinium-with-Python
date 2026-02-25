*** Settings ***
Library    Collections

*** Variables ***
${NAME}        Maneesha
${CITY}        Hyderabad
@{FRUITS}      Apple    Banana    Mango
&{USER}        name=Maneesha    age=25    city=Hyderabad

*** Test Cases ***
Variables Practice

    # 1. Print scalar variable
    Log    ${NAME}

    # 2. Assign two numbers and print their sum
    ${num1}    Set Variable    10
    ${num2}    Set Variable    20
    ${sum}     Evaluate    ${num1} + ${num2}
    Log    Sum is: ${sum}

    # 3. Use CITY variable inside sentence
    Log    I live in ${CITY}.

    # 4. Reassign variable value
    ${status}    Set Variable    Active
    Log    Initial Status: ${status}
    ${status}    Set Variable    Inactive
    Log    Updated Status: ${status}

    # 5. Print first item from list
    Log    First Fruit: ${FRUITS}[0]

    # 6. Loop through list and print each element
    FOR    ${fruit}    IN    @{FRUITS}
        Log    ${fruit}
    END

    # 7. Find length of list
    ${length}    Get Length    ${FRUITS}
    Log    List Length is: ${length}

    # 8. Print one dictionary key value
    Log    User Name: ${USER}[name]

    # 9. Add new key-value pair to dictionary
    Set To Dictionary    ${USER}    country=India
    Log    Updated Dictionary: ${USER}

    # 10. Loop through dictionary and print key & value
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} : ${value}
    END