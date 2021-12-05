using System;
using System.IO;
using System.Collections.Generic;

namespace _2015_03
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePuzzle(">")); // Expecting: 2
            Console.WriteLine(solvePuzzle("^>v<")); // Expecting: 4
            Console.WriteLine(solvePuzzle("^v^v^v^v^v")); // Expecting: 2
            Console.WriteLine(solvePuzzle(File.ReadAllText(@".\input.txt"))); // Expecting: 2592
        }

        static int solvePuzzle(string input) {
            Coordinates startingPoint = new Coordinates(0,0);
            List<House> neighborhood = new List<House>();
            House house = new House(startingPoint);
            neighborhood.Add(house);
            Coordinates santasPosition = new Coordinates(0,0);
            foreach( char c in input ) {
                switch (c) {
                    case '>': santasPosition.X++; break;
                    case '^': santasPosition.Y++; break;
                    case '<': santasPosition.X--; break;
                    case 'v': santasPosition.Y--; break;
                }
                if(Contains(neighborhood, santasPosition)) {
                    house.AddPresent();
                } else {
                    House newHouse = new House(santasPosition);
                    neighborhood.Add(newHouse);
                }
            }
            int luckyHouses = 0;
            foreach(House h in neighborhood) {
                if(h.Presents > 0) {
                    luckyHouses++;
                }
            }
            return luckyHouses;
        }

        static bool Contains(List<House> inHouses, Coordinates inPosition) {
            foreach(House house in inHouses) {
                if((house.Position.X == inPosition.X) && (house.Position.Y == inPosition.Y)) {
                    return true;
                }
            }
            return false;
        }
    }
}