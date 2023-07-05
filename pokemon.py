#Explanation of the program
#this is a pokemon battle




#ramdom module to call str() abd int() ramdomly
import random

#rules of the Game
#1.the system is going to give you 2 pokemons to battle each other
def pokemon_battle():
    pokemon = ['Bulbasaur','Charmander', 'Squirtle', 'Butterfly', 'Weedle', 'Pidgey' ]
    arena_battle = ['air','ocean','fire','forest']
#set a list of pokemon and display pokemon randomly
    pokemon_chose_a = random.choice(pokemon)
    pokemon_chose_b = random.choice(pokemon)
#choosing the level of the pokemon
    pokemon_level_a = random.randrange(11)
    pokemon_level_b = random.randrange(11)
#2 the life point of each pokemon is 20.
########start from 20 life point and finish games after life point is <=0
    life_point_a = 20
    life_point_b = 20
#choose arena randomly
    arena_chose = random.choice(arena_battle)
#displaying pokemon, level and arena.
    print(pokemon_chose_a,pokemon_level_a)
    print(pokemon_chose_b, pokemon_level_b)
    print('arena:', arena_chose)
    ###creating a dictionary with pokemon_a as a value and pokemon and level_a as a key (do it with a and b)
    pokemon_level = {
        pokemon_chose_a:pokemon_level_a,
        pokemon_chose_b:pokemon_level_b
    }
    ########while life_point_a >=0 and life_point_b >=0:

#3 when taking life point consider:
# A.kind of pokemon that are battling
    pokemon_kind = {
        'Bulbasaur': 'bug',
        'Charmander': 'fire',
        'Squirtle': 'water',
        'Butterfly': 'fly',
        'Weedle': 'bug',
        'Pidgey': 'fly'
    }

 #pokemon power according to arena
    kind_power = {
        "Charmander": "fire",
        'Squirtle': "ocean",
        "Bulbasaur": "ocean",
        "Weedle": "forest",
        "Butterfly": "forest",
        'Pidgey': "air"
    }
    pokemon_number_type = {
        "Charmander": 1,
        'Squirtle': 2,
        "Bulbasaur": 0,
        "Weedle": 0,
        "Butterfly": 0,
        'Pidgey': 3
    }
#Aif pokemon is in advantage, It take extra .5

        #if pokemons level are 0 then stop the program
    #while life_point_a > 0 and life_point_b > 0:#################################
    if pokemon_level_a == 0 and pokemon_level_b == 0:
        pass
        #taking .5 if pokemon type is better#######ERROR DONT GIVE A NUMBER JUST THE KIND OF POKEMON#####
        ####
    while life_point_a > 0 and life_point_b > 0:###############################################
             if pokemon_number_type[pokemon_chose_a] > pokemon_number_type[pokemon_chose_b]:
                 life_point_b -= 1.5
                 life_point_a -= 0.5
                 print(life_point_b, pokemon_chose_b)
                 print(life_point_a, pokemon_chose_a)
             #elif pokemon_number_type[pokemon_chose_a] == pokemon_number_type[pokemon_chose_b]:
                 #pass

             else:
                 life_point_a -= 1.5
                 life_point_b -= 0.5
                 print(life_point_a,pokemon_chose_a)
                 print(life_point_b, pokemon_chose_b)

#B.level of pokemon######ERRROR you are checking the the pokemon level (GOOD) but then you are taking .5 from the less life_point
    while life_point_a > 0 and life_point_b > 0:
             if abs((pokemon_level_a - pokemon_level_b)) == 0:
                 pass
             elif abs((pokemon_level_a - pokemon_level_b)) >= 1 and abs((pokemon_level_a - pokemon_level_b)) <= 2:
                 if pokemon_level[pokemon_chose_a] > pokemon_level[pokemon_chose_b]:
                     life_point_b-=1.5
                     life_point_a -= 0.5
                     print(life_point_b,pokemon_chose_b )
                     print(life_point_a, pokemon_chose_a)
                 elif pokemon_level[pokemon_chose_b] > pokemon_level[pokemon_chose_a]:
                     life_point_a -= 1.5
                     life_point_b -= 0.5
                     print(life_point_a, pokemon_chose_a)
                     print(life_point_b, pokemon_chose_b)


             elif abs((pokemon_level_a - pokemon_level_b)) >= 3 and abs((pokemon_level_a - pokemon_level_b)) <= 4:
                  if pokemon_level[pokemon_chose_a] > pokemon_level[pokemon_chose_b]:
                       life_point_b -= 1.5
                       life_point_a -= 0.5
                       print(life_point_b, pokemon_chose_b)
                       print(life_point_a, pokemon_chose_a)
                  elif pokemon_level[pokemon_chose_b] > pokemon_level[pokemon_chose_a]:
                       life_point_a -= 1.5
                       life_point_b -= 0.5
                       print(life_point_a, pokemon_chose_a)
                       print(life_point_b, pokemon_chose_b)
            #new_value = min(life_point_b, life_point_a) - 1
            #print(min(life_point_b,life_point_a), "<---&This is the pokemon level min and new life point -->",new_value)
            #pass
             elif abs((pokemon_level_a - pokemon_level_b)) >= 5 and abs((pokemon_level_a - pokemon_level_b)) <= 6:
                if pokemon_level[pokemon_chose_a] > pokemon_level[pokemon_chose_b]:
                    life_point_b -= 2
                    life_point_a -= 0.5
                    print(life_point_b, pokemon_chose_b)
                    print(life_point_a, pokemon_chose_a)
                elif pokemon_level[pokemon_chose_b] > pokemon_level[pokemon_chose_a]:
                    life_point_a -= 2
                    life_point_a -= 0.5
                    print(life_point_a, pokemon_chose_a)
                    print(life_point_b, pokemon_chose_b)
            #new_value = min(life_point_b, life_point_a) - 1.5
            #print(min(life_point_b,life_point_a), "<---*This is the pokemon level min and new life point -->",new_value)

                else:
                    if pokemon_level[pokemon_chose_a] > pokemon_level[pokemon_chose_b]:
                        life_point_b -= 2.5
                        life_point_a -= 0.5
                        print(life_point_b, pokemon_chose_b)
                        print(life_point_a, pokemon_chose_a)
                    elif pokemon_level[pokemon_chose_b] > pokemon_level[pokemon_chose_a]:
                        life_point_a -= 2
                        life_point_b -= 0.5
                        print(life_point_a, pokemon_chose_a)
                        print(life_point_b, pokemon_chose_b)
            #new_value = min(life_point_b, life_point_a) - 1.5
            #print(min(life_point_b,life_point_a), "<---@This is the pokemon level min and new life point -->",new_value)

#C.Arena

    while life_point_a > 0 and life_point_b > 0:
             if arena_chose == kind_power[pokemon_chose_a]:
                life_point_b -=1
                life_point_a -= 0.5
                print(life_point_b,pokemon_chose_b )
                print(life_point_a, pokemon_chose_a)
             elif arena_chose == kind_power[pokemon_chose_b]:
                life_point_a -=1
                life_point_b -= 0.5
                print(life_point_a,pokemon_chose_a)
                print(life_point_b, pokemon_chose_b)
             else:
                pass
    if life_point_a > life_point_b:
        print(pokemon_chose_a, "WINS")
    else:
        print(pokemon_chose_b, "WINS")
#create a list with arena of pokemon if pokemon is in his natural environment
#create a dictionary with pokemon and associate with the arena, this is extra .5 points


#if pokemon is stronger than the other then take extra .5

#how make first pokemon attack and then second pokemon?
pokemon_battle()

