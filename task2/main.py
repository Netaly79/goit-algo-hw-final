import turtle


def draw_tree(length, t, level):
    if level == 0:
        return
    else:
        t.forward(length)

        position = t.pos()
        head = t.heading()

        t.right(45)
        draw_tree(0.6 * length, t, level - 1)

        t.setpos(position)
        t.setheading(head)

        t.left(45)
        draw_tree(0.6 * length, t, level - 1)

        t.setpos(position)
        t.setheading(head)

        t.backward(length)


def main():
    level = int(input("Кількість проміжних гілочок: "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(5)
    t.color("green")
    t.pensize(1)

    t.penup()
    t.setpos(0, -200)
    t.pendown()
    t.left(90)

    draw_tree(200, t, level)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()
