from turtle import * 


#we want to paint a house

#step 1:  drawing a square 
shape("turtle")
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of drawing a square

#drawing a door
forward(70)
color
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
#end of drawing a door

#drawing a roof 
penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing a roof

#drawing a window N1
penup()
goto(10, 90)
pendown()

color("pink")
right(240)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

color("pink")
penup()
goto(10, 115)
pendown()
left(90)
forward(50)

penup()
goto(35, 90)
pendown()
left(90)
forward(50)
#end of drawing a window N1

#drawing a window N2
penup()
goto(140, 90)
pendown()

right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(140, 115)
pendown()

left(90)
forward(50)

penup()
goto(165, 90)
pendown()

left(90)
forward(50)
#end of drwaing windwn N2

color("black")
penup()
goto(115, 50)
pendown()

exitonclick()