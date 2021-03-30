using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class SpecialOfferDTO
    {
        public int SpecialOfferId { get; set; }
        public string ProductName { get; set; }
        public double PriceInEuro { get; set; }
        public string Size { get; set; }
        public double DiscountInEuro { get; set; }

        public List<BranchDTO> Branches { get; set; }

    }
}