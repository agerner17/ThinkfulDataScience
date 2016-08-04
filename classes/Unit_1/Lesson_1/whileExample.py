walker1 = 0

walker2 = 102

walking = True


while walking:
   if walker1<=102:
      print("Walker 1 has traveled {}".format(walker1))
      walker1 = walker1 +2

      if walker2 > 0:
         print("Walker 2 is still {} miles away".format(walker2))
         walker2 = walker2 - 1

         if walker1==walker2:
            print("Walker 1 and 2 have met at mile {}".format(walker1))

            break
            
   else:
      walking = False
else:
   print("Whew!")