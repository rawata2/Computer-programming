using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class SpecialOffer
    {
        private ICollection<Branch> _branches;
        public SpecialOffer()
        { _branches = new List<Branch>(); }

        public int SpecialOfferId { get; set; }
        public string ProductName { get; set; }
        public double PriceInEuro { get; set; }
    public string Size { get; set; }
    public double DiscountInEuro { get; set; }

public virtual ICollection<Branch> Branches
{
    get { return _branches; }

    set { _branches = value; }
}
    }
}

