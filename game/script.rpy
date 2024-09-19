# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("You")         # Main character
define n = Character("")            # Narrator
define f = Character("Friend", color="#c8c8ff") # Friend
default placeholder_name = "PLACEHOLDER"



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "{i}Here I am.{/i}"

    e "{i}I left everything to come here. This is my last chance to make things right.{/i}"

    e "{i}I can't mess this up.{/i}"

    n "You walk through the gate of your new school, ready to start fresh."

    n "You're determined to make the most of this opportunity."

    n "You're feeling..."

    menu:
        "Nervous": 
            jump nervous
        "Confident": 
            jump confident
    
    label confident:
        e "Ok, this should be fine."

        n "It wasn't."                      # TODO: a real branch here

        jump nervous

    label nervous:
        e "{i}Shit! I don't know what to do...{/i}"

        e "{i}I should just head straight to the classroom.{/i}"

        n "You enter the class first, while all the other students are already making friends outside."

        e "{i}If you're here, that means you deserve it, right?{/i}"

        e "{i}Should be easy for me to blend in. I'm gonna talk to the first person to enter the room.{/i}"

        e "{i}I should text mom to let her know everything's fine at uni.{/i}"

        n "As soon as you send her the text, you discover a new app you never seen before on your phone."

        e "{i}What the fuck is Z.B.E.U.L. Land?{/i}"

        menu:
            "Open it":
                jump app
            "Uninstall it":
                jump uninstall
    

    label uninstall:
        n "You press your finger on the app for a few seconds but nothing appears."

        n "You decide to give it a try and press the icon."

        jump app

    label app:
        e "{i}Welcome to ZBEUL... OK. Please read... I agree.{/i}"

        e "{i}Oh it's just the app of the uni, but how did it get on my phone?{/i}"

        n "A strange voice interupts your thinking."

        f "Hey, my name is [placeholder_name], what's yours?"

        e "{i} Who's this weirdo? {/i}"

        e "{i} I said I was gonna talk to the first PERSON to enter. {/i}"

        f "Do-You-English?"

        e "Oh shit yeah sorry. I'm "

        jump enter_name

    label enter_name:
        $ player_name = False
        while not player_name:
            $ player_name = renpy.input("Enter your name:")
            $ player_name = player_name.strip()
            $ e = Character(player_name)
            if not player_name:
                n "Not even funny."

        f "What are you doing all alone [player_name]?"

        e "Same goes for you doesn't it?"


    # This ends the game.

    return
