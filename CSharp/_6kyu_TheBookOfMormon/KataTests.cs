namespace _6kyu_TheBookOfMormon
{
    using NUnit.Framework;

    [TestFixture]
    public class KataTests
    {
        [Test]
        public void BasicTest1()
        {
            Assert.AreEqual(0, Kata.Mormons(10, 3, 9)); // No missions are needed because the number of followers already exceeds target
        }

        [Test]
        public void BasicTest2()
        {
            Assert.AreEqual(1, Kata.Mormons(40, 2, 120));
        }

        [Test]
        public void BasicTest3()
        {
            Assert.AreEqual(2, Kata.Mormons(40, 2, 121));
        }

        [Test]
        public void BasicTest4()
        {
            Assert.AreEqual(12, Kata.Mormons(20000, 2, 7000000000)); // Mormons dominate the world!
        }
    }
}