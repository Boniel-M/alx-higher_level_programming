import unittest
import json
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 3)
        expected_output = "###\n" \
                          "###\n" \
                          "###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 2/3 - 5/10")

    def test_update_args(self):
        r = Rectangle(5, 10)
        r.update(7, 3, 4, 1, 2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_update_kwargs(self):
        r = Rectangle(5, 10)
        r.update(id=7, width=3, height=4, x=1, y=2)
        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n" \
                          "###\n" \
                          "###\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_str(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(str(s), "[Square] (1) 2/3 - 5")

    def test_update_args(self):
        s = Square(5)
        s.update(7, 3, 1, 2)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=7, size=3, x=1, y=2)
        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)


class TestBase(unittest.TestCase):
    def test_constructor_with_id(self):
        b = Base(1)
        self.assertEqual(b.id, 1)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string(self):
        b = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"key": "value"}]), '[{"key": "value"}]')
        self.assertEqual(Base.to_json_string([{"key": "value"}, {"key2": "value2"}]), '[{"key": "value"}, {"key2": "value2"}]')

    def test_save_to_file(self):
        b1 = Base()
        b2 = Base()
        Base.save_to_file([b1, b2])
        with open("Base.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [{"id": 1}, {"id": 2}])

        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [])

    def tearDown(self):
        try:
            os.remove("Base.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()

