
def start():
    print("Welcome, my names Lisa and I run this bakery. Would you like to work here?")
    answer=input("yes or no?\n")
    if answer=="yes":
        print("Great, but I didn't get your name. What is it?")
        your_name=input("")
        print("Nice to meet you" + " " + your_name)
        chapter1()
    else:
        print("Goodbye")
def chapter1():
    Intro=""" Welcome to my bakery Lisa's Sweets and Treats, I'm the owner here.
    Im going on vacation and need someone to take over my store whle I'm gone. You might 
    meet some intresting characters while working here, but overall its an easy job. Do you 
    have any questions?     
    """
    questions="""Select 1 2 or 3
    1.That sounds great I can take it from here.
    2.Where are you going on vacation?
    3.What do you mean intresting characters?
    """
    print(Intro)
    print(questions)
    choice=input("1 2 3\n")
    if choice=="1":
        print("all right I will leave you to it")
        chapter2()
    if choice=="2":
        print("Lisa: I am glad you asked, I'm visting an old friend")
        print("Me: what friend? where do the live?")
        print("Lisa: I don't think we're well aquainted enough, for you to know that. I'm off now, BYE!!!")
        chapter2()
    if choice=="3":
        print("Lisa: You will see soon enough. *wink* I have to get going or I'll be late. BYE!! ")
        print("Me:W-W-Wait")
        chapter2()
def chapter2():
    print("Alright, looks like I'm on my own now. What should I do first?")
    what_to_do="""Select 1 or 2 
    1. I should probably organize and clean
    2. It doesn't look like there will be many customers today maybe I should just take a nap.
    """
    print(what_to_do)
    choice=input("1 or 2\n")
    if choice=="1":
        print("while cleaning your first customer walks in")
        chapter3_v1()

    else:
        print("You wake up from your nap to find out the store has been robbed. Oh No! What will you do?")
        robbed= """ Select 1 or 2
        1. Call Lisa and apoligize
        2.Don't tell Lisa and find who stole the money before she gets back
        """
        print(robbed)
        decide=input("1 or 2\n")
        if decide=="1":
            print("Lisa was dissappointed in you and decided it would be best if she fired you and came back home\n")
            print("Oh No! what will you do you've been fired on your first day! Lucky for you, you can travel through time")
            replay="""Select 1 or 2 
            1.Replay chapter from the start
            2.Replay game from the begining 
            """
            print(replay)
            wwyd=input("1 or 2\n")
            if wwyd=="1":
                chapter2()
            else:
                start()
        else:
            print("I'll find the theif and return the money before anyone realizes")
            chapter3_v2()
def chapter3_v1():
    print("Me: Hello, welcome to Lisa's bakery. How may I help you?")
    print("Customer: Can I get a bluberry muffin and a small coffee?")
    print("Me: one bluberry muffin coming right up?")
    coffee = """Looks like your out of coffee. What will you do? Select 1 or 2
    1. Make more
    2.Inform the customer you have no more coffee"""
    print(coffee)
    coffee_choice=input("1 or 2\n")
    if coffee_choice=="1":
        print("The coffee machine is broken. What will you do?")
        broken_coffee="""Select 1 or 2
        1.Fix the coffee machine
        2.Explain to the customer"""
        print(broken_coffee)
        broke_cafe=input("1 or 2\n")
        if broke_cafe=="1":
            print("Congrats!! You where able to fix it and the customer went on their way. You've made your first sale!!!")
            #callch4v1
        else:
            print("You expain to the customer and the offer to fix the coffee machine. Will you let them fix it? yes or no?")
            fix=input("yes or no\n")
            if fix=="yes":
                print("You notice the customer has a strange accent when they speak")
                #callch4v2        
            else:
                print("The customer said fine and walked out with their muffin")
                #callch4v3
    else:
        print("The customer is annoyed and ask how can you be out of coffee so early. You apologize, but they leave annoyed")
            #callch4v3
def chapter3_v2():
    print("Your first customer walks in while your thinking of ways to capture the theif")
    wwyd="""Select 1,2 or 3
    1. Tell the customer to wait and look at the cameras 
    2. Tell the customer to wait and search for clues 
    3. Attend to the customer and wait till the end of the day to search for clues
    """
    print(wwyd)
    search=input("1,2 or 3\n")
    if search == "1":
        print("test")
        #call adventure mode 1
    if search == "2":
        print("test2")
        #call adventure mode 2
    if search == "3":
        print("test3")
        #call adventure mode 3
#start game
start()
