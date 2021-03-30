using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class Customer
    {
        private ICollection<Product> _products;

        public Customer()
        {
            _products = new List<Product>();
        }

        public int CustomerId { get; set; }

        public string Name { get; set; }
        public int PhoneNumber { get; set; }
        public string Gender { get; set; }
        public int AgeInYears { get; set; }

        public virtual ICollection<Product> Products
        {
            get { return _products; }

            set { _products = value; }
        }
    }
}