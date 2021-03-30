namespace Health.Migrations
{
    using Models;
    using System;
    using System.Collections.Generic;
    using System.Data.Entity;
    using System.Data.Entity.Migrations;
    using System.Linq;

    internal sealed class Configuration : DbMigrationsConfiguration<Health.Models.PowerContext>
    {
        public Configuration()
        {
            AutomaticMigrationsEnabled = true;
            ContextKey = "Health.Models.PowerContext";
        }

        protected override void Seed(Health.Models.PowerContext context)
        {
            //  This method will be called after migrating to the latest version.

            //  You can use the DbSet<T>.AddOrUpdate() helper extension method 
            //  to avoid creating duplicate seed data. E.g.
            //
            //    context.People.AddOrUpdate(
            //      p => p.FullName,
            //      new Person { FullName = "Andrew Peters" },
            //      new Person { FullName = "Brice Lambson" },
            //      new Person { FullName = "Rowan Miller" }
            //    );
            //
            var products = new List<Product>
            {
            new Product{Name="Aloe Vera",PriceInEuro=20,Size= "Small",Description="It can be used to cure burns" },
            new Product{Name="Vitamin tablets",PriceInEuro=20,Size="Small",Description="It is essential for veryday life " },
            new Product{Name="vitamin Oil",PriceInEuro=20,Size="Medium",Description="It can also be used to cure burn" },
            new Product{Name="Ginger ",PriceInEuro=20,Size="Large",Description="Good for heart" },
            new Product{Name="Avogel",PriceInEuro=20,Size="Medium",Description="Cold and flu" },


                };

            products.ForEach(s => context.Products.Add(s));
            context.SaveChanges();


            var customers = new List<Customer>
            {
            new Customer{Name="Mark",AgeInYears=10 ,
Products= products.Where(b =>(b.Name == "Aloe Vera") || (b.Name == "AVogel")).ToList() },
             new Customer{Name="paul",AgeInYears=10 ,
Products= products.Where(b =>(b.Name == "Viatmin tablets") || (b.Name == "Ginger")).ToList() },

 new Customer{Name="Ben",AgeInYears=10 ,
Products= products.Where(b =>(b.Name == "Ginger") || (b.Name == "Vitamin tablet")).ToList() },

 new Customer{Name="Tara",AgeInYears=10 ,
Products= products.Where(b =>(b.Name == "Avogel") || (b.Name == "Aloe Vera")).ToList() },





                };

            customers.ForEach(s => context.Customers.Add(s));
            context.SaveChanges();

        }
    }
}




   