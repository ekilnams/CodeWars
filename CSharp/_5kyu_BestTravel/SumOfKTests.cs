namespace _5kyu_BestTravel.Tests
{
    using NUnit.Framework;
    using System.Collections.Generic;

    [TestFixture]
    public class SumOfKTests
    {

        [Test]
        public void Test1()
        {
            List<int> ts = new List<int> { 50, 55, 56, 57, 58 };
            int? n = SumOfK.chooseBestSum(163, 3, ts);
            Assert.AreEqual(163, n);
        }

        [Test]
        public void Test2()
        {
            List<int> ts = new List<int> { 50 };
            int? n = SumOfK.chooseBestSum(163, 3, ts);
            Assert.AreEqual(null, n);
        }

        [Test]
        public void Test3()
        {
            List<int> ts = new List<int> { 91, 74, 73, 85, 73, 81, 87 };
            int? n = SumOfK.chooseBestSum(230, 3, ts);
            Assert.AreEqual(228, n);
        }

        [Test]
        public void Test4()
        {
            List<int> ts = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
            int? n = SumOfK.chooseBestSum(27, 6, ts);
            Assert.AreEqual(27, n);
        }
    }
}