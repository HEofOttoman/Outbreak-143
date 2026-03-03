
define T = Character ("Tara")
define You = Character ("You")
define C = Character ("Captain",image ="captain")
define J = Character ("Jasper")

label start:
   scene bg
   You "It seems I've woken up in an unfamiliar environment.."
   scene inroom
   T "Oh, finally.. you've woken up!"
   You "Where the hell am I?"
   T "Oh come on silly.. Don't you remember?"
   You "..."
   T "The company put us under cause the trip is so long!"
   T "In case your memory needs jogging, I'm the chef of this ship, my name is Tara!"
   T "Take a look at your own ID to remember yourself!"
   scene idcard
   You "What the heck! It's all broken!"
   scene inroom
   T "Oh my, why don't we just call you by your ID number?"
   # 00143
   # T "Mr. 00143"
   show captain
   C "You awake now eh?"
   C "Lets get this over an' done with!"
   C "We know the previous crew that came down here died from *that* disease"
   C "Remember to look out for the symptoms.."
   C "Bleeding from the ears gums or fingernails."
   C "Itchy, red eyes,"
   C "And emotional outbursts."
   C "But we're going to do far better than them."
   scene algae 
   C "I'm going to go get the first sample."
   scene sandy
   T "Be safe out there captain!"
   scene collect 
   You "I hope it goes well.."
   scene cut 
   You "..."
   scene hallway
   show captain
   C "I'm back"
   T "I'm so glad youre back in one piece Captain!"
   C "Me too. but we need to spend a night here before we can go back to the surface."
   T "It's getting late, it's probably time to go to bed"
   You "*You go to bed*"
   scene doorway
   C "BANG!"
   You "What is that sound?!"
   You "Captain.. what are you doing here?"
   C "unghhh"
   You "Captain, what's wrong? Are you alright?"
   You "AHH! Captain!! What the hell!"
   You "Is this what happened to the last crew that came here?!"
   You "*Running to the freezer room*"
   scene freezer
   C "ughhhhhuhhhhh *hiss*"
   menu:
      "shove him in": 
         pass
      "SHOVE HIM IN": 
         pass
   scene hands
   You "I better go tell everyone about this! He's crazy!!"
   scene hallway
   You "*After an anxious rest you wake up and meet up with the crew*"
   T "Good morning my sweetheart!"
   
   show tara_happy
   show jasper
   You "The Captain has gone insane, I think he has the infection."
   show tara_sad
   J "Well we can't just leave him in there"
   show jasper
   menu:
      "Offer to help.": 
         You "I'll look after him, don't worry about it!"
         scene infected
         You "The disease spreads to you from the Captain, killing you slowly. It feels almost like you are suffocating"
      "Tell Tara to do it.":
         scene
         You "Tara, could you please go check up on him, he seems like he has a soft spot for you."
         T "I would love to, I'll go there right away."
         You "*Hours pass and you talk to Jasper.*"
         show jasper
         You "Jasper, I think that Tara has the infection. She's been looking sad and has been staying in her room for hours and everytime I've seen her eyes have been bloodshot"
         J "*Scared* so you want me to kill her??"
         You "I just don't want her to suffer.. she's so sweet."
         J "Aghh I guess youre right.."
         You "Jasper gets his gun and you hear a brief conversation."
         J "Tara, I'm sorry, I think you're so amazing and I've loved seeing you.."
         show tara_sad
         T "What do you mean.. *frantically* Jasper!"
         You "*A loud bang rings through your ears."
         You "*Days pass and the realisation hits you, you cannot go to the suface without the captain."
         You "Youve been avoiding Jasper ever since you told him to kill Tara"         
         You "It just hasnt been the same without her."
         You "You may as well be proactive with your situation"
         menu:
            "Stay in your room trying to find a cure":
               You "You've been in your room for weeks, in the mirror you look tired and sad..."
               You "You see that your eyes are bloodshot and they feel itchy, your ears are graced with a thin stream of blood and your nails are deep scarlet."
               scene infected
               You "You Died."
            "Try to drive the submarine.":
               You "You go into the cockpit of the submarine and are greeted with an array of pretty lights and buttons, none of them make sense."
               You "The remaining crew is growing ever suspicious of you. you have genuinely had enough of their constant nagging and comments on your state."
               You "The knife in the pockets of your pants glimmers, and you hold it tight, slashing jaspers chest and gouging out the eyes of the captain."
               scene kill
               You "You go manic, and die."
         
      
      
      
         

      
      
      