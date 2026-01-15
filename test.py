import unittest
import main


class TestJeuDeLaVie(unittest.TestCase):

    def test_grid_initialized(self):
        #Given
        jeu = main.JeuDeLaVie()

        #When
        grid = jeu.get_grid()

        #Then
        self.assertEqual(grid, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_cell_initialized(self):
        #Given
        jeu = main.JeuDeLaVie()

        #When
        jeu.add_cell(0, 0)
        grid = jeu.get_grid()

        #Then
        self.assertEqual(grid, [[1, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_cell_dead(self):
        #Given
        jeu = main.JeuDeLaVie()

        jeu.add_cell(0, 0)

        #When
        jeu.remove_cell(0, 0)
        grid = jeu.get_grid()

        #Then
        self.assertEqual(grid, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_alone_cell(self):
        #Given
        jeu = main.JeuDeLaVie()

        jeu.add_cell(0, 0)

        #When
        neighbours = jeu.check_neighbours(0, 0)

        #Then
        self.assertEqual(neighbours, 0)

    def test_one_neighbour_cell(self):
        # Given
        jeu = main.JeuDeLaVie()

        jeu.add_cell(0, 0)
        jeu.add_cell(0, 1)

        # When
        neighbours = jeu.check_neighbours(0, 0)
        # Then
        self.assertEqual(neighbours, 1)

    def test_iteration_square(self):
        # Given
        jeu = main.JeuDeLaVie()
        jeu.add_cell(0, 0)
        jeu.add_cell(0, 1)
        jeu.add_cell(1, 0)
        jeu.add_cell(1, 1)
        # [[1, 1, 0],
        #  [1, 1, 0],
        #  [0, 0, 0]]
        # When
        jeu.iteration()
        # Then
        grid = jeu.get_grid()
        self.assertEqual(grid, [[1, 1, 0], [1, 1, 0], [0, 0, 0]])

    def test_iteration_more_than_and_equal_3(self):
        # Given
        jeu = main.JeuDeLaVie()
        jeu.add_cell(0, 0)
        jeu.add_cell(0, 1)
        jeu.add_cell(1, 0)
        jeu.add_cell(1, 1)
        jeu.add_cell(0, 2)

        # [[1, 1, 1],
        #  [1, 1, 0],
        #  [0, 0, 0]]

        # When
        jeu.iteration()
        # Then
        grid = jeu.get_grid()
        self.assertEqual(grid, [[1, 0, 1], [1, 0, 1], [0, 0, 0]])

    def test_iteration_less_than_2(self):
        # Given
        jeu = main.JeuDeLaVie()
        jeu.add_cell(0, 0)
        jeu.add_cell(0, 1)

        # [[1, 1, 0],
        #  [0, 0, 0],
        #  [0, 0, 0]]

        # When
        jeu.iteration()
        # Then
        grid = jeu.get_grid()
        self.assertEqual(grid, [[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def test_life_cycle(self):
        # Given
        jeu = main.JeuDeLaVie()
        jeu.add_cell(0, 0)
        jeu.add_cell(0, 1)
        jeu.add_cell(1, 0)
        jeu.add_cell(1, 2)
        jeu.add_cell(2, 2)

        # [[1, 1, 0],
        #  [1, 1, 1],
        #  [0, 0, 1]]

        # [[1, 0, 1],
        #  [1, 0, 1],
        #  [0, 0, 1]]

        # [[0, 0, 0],
        #  [0, 0, 1],
        #  [0, 1, 0]]

        # When
        jeu.iteration()
        # Then
        grid = jeu.get_grid()
        self.assertEqual(grid, [[0, 0, 0], [0, 0, 1], [0, 1, 0]])


if __name__ == '__main__':
    unittest.main()
