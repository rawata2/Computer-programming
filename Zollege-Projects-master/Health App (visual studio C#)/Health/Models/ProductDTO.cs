using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class ProductDTO
    {
        public int ProductId { get; set; }

        public string Name { get; set; }
        public double PriceInEuro { get; set; }
        public string Size { get; set; }

        public string Description { get; set; }
        public List<CustomerDTO> Customers { get; set; }
    }
}