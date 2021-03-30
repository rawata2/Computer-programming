using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class Product
    {
        private ICollection<Customer> _customers;

        public Product()
        {
            _customers = new List<Customer>();
        }

        public int ProductId { get; set; }

        public string Name { get; set; }
        public double PriceInEuro { get; set; }
        public string Size { get; set; }

        public string Description { get; set; }

        public virtual ICollection<Customer> Customers
        {
            get { return _customers; }

            set { _customers = value; }
        }
    }
}
