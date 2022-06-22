namespace _5kyu_TheHungerGames_ZooDisaster
{
    using System.Collections.Generic;
    using System.Linq;

    class Dinglemouse
    {
        private static readonly Dictionary<string, List<string>> _dietLookup = new()
        {
            { "antelope", new() { "grass" } },
            { "big-fish", new() { "little-fish" } },
            { "bug", new() { "leaves" } },
            { "bear", new() { "big-fish", "bug", "chicken", "cow", "leaves", "sheep" } },
            { "chicken", new() { "bug" } },
            { "cow", new() { "grass" } },
            { "fox", new() { "chicken", "sheep" } },
            { "giraffe", new() { "leaves" } },
            { "lion", new() { "antelope", "cow" } },
            { "panda", new() { "leaves" } },
            { "sheep", new() { "grass" } }
        };

        private static bool AttemptEat(string animal, string target)
        {
            List<string> diet;
            if (_dietLookup.TryGetValue(animal, out diet))
            {
                return diet.Contains(target);
            }
            return false;
        }

        public static string[] WhoEatsWho(string zoo)
        {
            List<string> history = new() { zoo };

            if (!string.IsNullOrWhiteSpace(zoo))
            {
                List<string> lineup = zoo.Split(',').ToList();
                bool somethingWasEaten;

                do
                {
                    somethingWasEaten = false;

                    for (int i = 0; i < lineup.Count; i++)
                    {
                        if (i > 0)
                        {
                            if (AttemptEat(lineup[i], lineup[i - 1]))
                            {
                                history.Add($"{lineup[i]} eats {lineup[i - 1]}");
                                lineup.RemoveAt(i - 1);
                                somethingWasEaten = true;
                                break;
                            }
                        }

                        if (i < lineup.Count - 1)
                        {
                            if (AttemptEat(lineup[i], lineup[i + 1]))
                            {
                                history.Add($"{lineup[i]} eats {lineup[i + 1]}");
                                lineup.RemoveAt(i + 1);
                                somethingWasEaten = true;
                                break;
                            }
                        }
                    }
                }
                while (somethingWasEaten);

                history.Add(lineup.Count > 1 ? string.Join(",", lineup.ToArray()) : lineup[0]);
            }

            return history.ToArray();
        }
    }
}
