using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class CustomerDTO
    {
        public int CustomerId { get; set; }
        public string Name { get; set; }
        public int PhoneNumber { get; set; }
        public string Gender { get; set; }
        public int AgeInYears { get; set; }

        public List<ProductDTO> Products { get; set; }

    }
}
