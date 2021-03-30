using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Data.Entity.ModelConfiguration.Conventions;
using Health.Models;

namespace Health.Models
{
    public class PowerContext : DbContext
    {
        public PowerContext() : base("PowerContext")
        {

        }

        public DbSet<Product> Products { get; set; }

        public DbSet<Customer> Customers { get; set; }

        public DbSet<Branch> Branches { get; set; }
        public DbSet<SpecialOffer> SpecialOffers { get; set; }
    }
}

