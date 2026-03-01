
define T = Character ("Tara")
define You = Character ("You")
define C = Character ("Captain",image ="captain")
define J = Character ("Jasper")
label start:
   scene bg
   You "it seems ive woken up in an unfamilliar enviorment"
   scene inroom
   T "Oh,finaly.. you've woken up!"
   You "Where the hell am I?"
   T "Oh come on silly.. dont you remeber?"
   You "..."
   T "The company put us under cause the trip is so long!"
   T "In case your memory needs jogging Im the chef of this ship, my name is Tara!"
   T "Take a look at your own ID to remeber yourself!"
   scene idcard
   You "What the heck! Its all broken!"
   scene inroom
   T "Oh my, why dont we just call you by your ID number?"
   show captain
   C "you awake now eh?"
   C "lets get this over an' done with!"
   C "we know the preivous crew that came down here died from *that* disease"
   C "remember to lookout for the symptoms.."
   C "bleeding from the ears gums or fingernails."
   C "itchy, red eyes."
   C "and emotional outbursts."
   C "but we're going to do far better than them."
   scene algae 
   C "im going to go get the first sample."
   scene sandy
   T "be safe out there captian!"
   scene collect 
   You "i hope it goes well.."
   scene cut 
   You "..."
   scene hallway
   show captain
   C "im back"
   T "im so glad youre back in one piece Captain!"
   C "me too. but we need to spend a night here before we can go back to the surface"
   T "its getting late, its probably time to go to bed"
   You "*you go to bed*"
   scene doorway
   C "BANG!"
   You "what is that sound?!"
   You "Captain.. what are you doing here?"
   C "unghhh"
   You "captain, whats wrong? are you alright"
   You "AHH! captain!! what the hell!"
   You "is this what happened to the last crew that came here?!"
   You "*running to the freezer room*"
   scene freezer
   C "Ughhhhhuhhhhh *hiss*"
   menu:
      "shove him in": 
         pass
      "SHOVE HIM IN": 
         pass
   scene hands
   You "i better go tell everyone about this! He's crazy!!"
   scene hallway
   You "*after an anxious rest you wake up and meet up with the crew*"
   T "Goodmorning my sweetheart!"
   
   show tara_happy
   show jasper
   You "the captain has gone insane, i think he has the infection."
   show tara_sad
   J "well we cant just leave him in there"
   show jasper
   menu:
      "offer to help.": 
         You "ill look after him, dont worry about it!"
         scene infected
         You "the disease spreads to you from the captain, killing you slowly, it feels almost like you are suffocating"
      "tell Tara to do it.":
         scene
         You "Tara, could you please go check up on him, he seems like he has a soft spot for you."
         T "i would love to, ill go there right away."
         You "*hours pass and you talk to Jasper.*"
         show jasper
         You "Jasper, i think that Tara has the infection. shes been looking sad and has been staying in her room for hours and everytime ive seen her eyes have been bloodshot"
         J "*scared* so you want me to kill her??"
         You "i just dont want her to suffer.. shes so sweet."
         J "aghh i guess youre right.."
         You "jasper gets his gun and you hear a breif conversation."
         J "Tara, im sorry, i think youre so amazing and ive loved seeing you.."
         show tara_sad
         T "what do you mean.. *frantically* jasper!"
         You "*a loud bang rings through your ears."
         You "*days pass and the realisation hits you, you cannot go to the suface without the captain."
         You "Youve been avoiding Jasper ever since you told him to kill Tara"         
         You "it just hasnt been the same without her."
         You " you may as well be proative with your situation"
         menu:
            "stay in your room trying to find a cure":
               You "youve been in your room for weeks, in the mirror you look tired and sad..."
               You "you see that your eyes are bloodshot and they feel itchy, your ears are graced with a thin stream of blood and your nails are deep scarlet."
               scene infected
               You "you died"
            "try to drive the submarine.":
               You "you go into the cockpit of the submarine and are greeted with an array of pretty lights and buttons, none of them make sense."
               You "the remaining crew is growing ever suspisous of you. you have genuinely had enough of their constant nagging and comments on your state."
               You "the knife in the pockets of your pants glimmers and you hold it tight, slashing jaspers chest and gauging out the eyes of the captian."
               scene kill
               You "you go manic and die."
         
      
      
      
         

      
      
      