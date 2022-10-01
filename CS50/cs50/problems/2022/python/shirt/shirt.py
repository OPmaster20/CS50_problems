from PIL import Image
import os
import sys
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments ")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
bao=os.path.splitext(sys.argv[2])
wu=os.path.splitext(sys.argv[1])

if wu[1] != bao[1]:
    sys.exit("Input and output have different extensions")
if bao[1]=='.jpg' or bao[1]=='.jpeg' or bao[1]=='.png':
    try:
        with Image.open(sys.argv[1]) as im:
            #shirt=Image.paste(im,mask=)
            #Image.save()
    except FileNotFoundError:
        sys.exit("Input does not exist")
else:
    sys.exit("Invalid output")



#valid=['j']
#valid2=['p']
#valid3=['g']
#valid4=['e']
#valid5=['n']
#for i in range(len(sys.argv[2])):

 #   if sys.argv[2][i] =='.':
  #      if (sys.argv[2][i+1] in valid and sys.argv[2][i+2] in valid2 and sys.argv[2][i+3] in valid3) or (sys.argv[2][i+1] in valid2 and sys.argv[2][i+2] in valid5 and sys.argv[2][i+3] in valid3) or (sys.argv[2][i+1] in valid and sys.argv[2][i+2] in valid2 and sys.argv[2][i+3] in valid4 and  sys.argv[2][i+4] in valid3):
   #         try:


    #        except:
     #           sys.exit("Input does not exist")
      #  else:
       #     sys.exit("Invalid output")
    #else:
       # sys.exit("Invalid output")
