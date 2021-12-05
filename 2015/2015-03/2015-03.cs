using System;
using System.IO;
using System.Collections.Generic;

namespace _2015_03
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(solvePuzzle(">", 2, 3));
            Console.WriteLine(solvePuzzle("^>v<", 4, 3));
            Console.WriteLine(solvePuzzle("^v^v^v^v^v", 2, 11));
            Console.WriteLine(solvePuzzle(File.ReadAllText(@".\input.txt"), 2592, 2360));
        }

        static string solvePuzzle(string Input, int Expected1, int Expected2) {
            string result = null;
            int answerPart1 = solvePuzzlePart1(Input);
            result  += printResults(1, answerPart1, Expected1);
            int answerPart2 = solvePuzzlePart2(Input);
            result  += printResults(2, answerPart2, Expected2);
            return result;
        }

        static string printResults(int Part, int Answer, int Expected) {
            string match = Answer == Expected ? "PASS" : "FAIL";
            string result = match + " : Part " + Part + " : Answer: " + Answer + " : Expected: " + Expected + "\n";
            return result;
        }

        static int solvePuzzlePart2(string input) {
            Coordinates startingPoint = new Coordinates(0,0);
            List<House> neighborhood = new List<House>();
            House house = new House(startingPoint);
            neighborhood.Add(house);
            Coordinates santasPosition = new Coordinates(0,0);
            Coordinates roboPosition   = new Coordinates(0,0);
            int index = 0;
            foreach( char c in input ) {
                if( index%2 == 0 ) {
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
                } else {
                    switch (c) {
                        case '>': roboPosition.X++; break;
                        case '^': roboPosition.Y++; break;
                        case '<': roboPosition.X--; break;
                        case 'v': roboPosition.Y--; break;
                    }
                    if(Contains(neighborhood, roboPosition)) {
                        house.AddPresent();
                    } else {
                        House newHouse = new House(roboPosition);
                        neighborhood.Add(newHouse);
                    }
                }
                index++;
            }
            int luckyHouses = 0;
            foreach(House h in neighborhood) {
                if(h.Presents > 0) {
                    luckyHouses++;
                }
            }
            return luckyHouses;
        }

        static int solvePuzzlePart1(string input) {
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