
#Calculate your BMI

 weight = int(input("Enter your Weight(kg):"))
 Height = int(input("Enter your Height (inch):"))
 Height_meter_sq = (Height * 0.0254) **2
 BMI = weight / Height_meter_sq # weight/height(sq.meter)
 print("Your BMI is:", BMI)

 if BMI <= 18 :
      print ("You are underweight !")
 elif  BMI >=18 and BMI <24 :
      print ("Your weight is normal ! ")
 else :
      print ("You are overweight ! ")





