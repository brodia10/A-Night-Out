msg = """
Scene opens up to a first person POV with a Character Named JAKE who will not talk.

JAKE is an introvert who never goes out but his friends always try and get him to do new and adventurous things to get him out of his bubble.

Scene-01
Jake is sitting in his apartment with nothing to do. Jake suddenly gets a text message from his best friend SCOTT.
Jake peers down at his phone and reads the text.
(Hey are you coming to JESSICA'S party?)

Jake looks at the text with dread because he knows his friends always guilt him into going out. Second text comes in from Frank before jake can even reply
(Come on man lives short you gotta get out of the house)

Scene pause Choice decisions on screen
Jake looks at this phone with two decisions
"""
img = """

             _.-----------._
          .-'      __       `-.
        .'       .'  `.        `.
       ;         :    :          ;
       |         `.__.'          |
       |   ___                   |
       |      JAKE'S PHONE       |
       | .---------------------. |
       | |    Choose 1 Or 2..  | |
       | |                     | |
       | |  1 - Ok I will go,  | |
       | |  only for a little  | |
       | |  bit.               | |
       | |                     | |
       | |  2 - I'm not feeling| |
       | |  it tonight.        | |
       | |                     | |
       | |                     | |
       | `---------------------' |
       |                         |
       |                __       |
        |_______________________|

       """
choices = {
    "a": {"choice": "Ok I will go... only for a little bit.", "img": img},
    "b": {"choice": "I'm not feeling it tonight.", "img": img},
}
