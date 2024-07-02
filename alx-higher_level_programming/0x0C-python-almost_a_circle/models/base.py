#!/usr/bin/python3
"""This module contains the 'Base' class and will be the “base” of all
   other classes in this project. The goal of it is to manage id attribute in
   all your future classes and to avoid duplicating the same code
   (by extension, same bugs)
"""
import json
import csv
import turtle


class Base:
    """This is the 'Base' class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes an instance of the 'Base' class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """This is a method that creates a new instance from key word args"""
        if cls.__name__ == "Rectangle":
            dummy = cls(22, 22)
        else:
            dummy = cls(22)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

    @staticmethod
    def to_json_string(list_dictionaries):
        """This is the serialization function"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """This is the deserialization function"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """This is the file i/o handling function to save the json string from
           a list of python dictionaries
        """
        with open("{}.json".format(cls.__name__), "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                new_list_objs = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(cls.to_json_string(new_list_objs))

    @classmethod
    def load_from_file(cls):
        """This is a method that deserializes JSON object to a Python object"""
        try:
            with open("{}.json".format(cls.__name__), "r") as jsonfile:
                json_string = jsonfile.read()
        except Exception:
            return []
        else:
            dict_objs = cls.from_json_string(json_string)
            instance_list = [cls.create(**dic) for dic in dict_objs]
            return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This is the csv equivalent"""
        with open("{}.csv".format(cls.__name__), "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This is the csv equivalent"""
        try:
            with open("{}.csv".format(cls.__name__), "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvf, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except Exception:
            return []
