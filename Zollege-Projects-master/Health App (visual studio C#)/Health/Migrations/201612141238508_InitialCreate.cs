namespace Health.Migrations
{
    using System;
    using System.Data.Entity.Migrations;
    
    public partial class InitialCreate : DbMigration
    {
        public override void Up()
        {
            CreateTable(
                "dbo.Branches",
                c => new
                    {
                        BranchId = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        Location = c.String(),
                        Established = c.DateTime(nullable: false),
                        SpecialOffer_SpecialOfferId = c.Int(),
                    })
                .PrimaryKey(t => t.BranchId)
                .ForeignKey("dbo.SpecialOffers", t => t.SpecialOffer_SpecialOfferId)
                .Index(t => t.SpecialOffer_SpecialOfferId);
            
            CreateTable(
                "dbo.Customers",
                c => new
                    {
                        CustomerId = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        PhoneNumber = c.Int(nullable: false),
                        Gender = c.String(),
                        AgeInYears = c.Int(nullable: false),
                    })
                .PrimaryKey(t => t.CustomerId);
            
            CreateTable(
                "dbo.Products",
                c => new
                    {
                        ProductId = c.Int(nullable: false, identity: true),
                        Name = c.String(),
                        PriceInEuro = c.Double(nullable: false),
                        Size = c.String(),
                        Description = c.String(),
                    })
                .PrimaryKey(t => t.ProductId);
            
            CreateTable(
                "dbo.SpecialOffers",
                c => new
                    {
                        SpecialOfferId = c.Int(nullable: false, identity: true),
                        ProductName = c.String(),
                        PriceInEuro = c.Double(nullable: false),
                        Size = c.String(),
                        DiscountInEuro = c.Double(nullable: false),
                    })
                .PrimaryKey(t => t.SpecialOfferId);
            
            CreateTable(
                "dbo.ProductCustomers",
                c => new
                    {
                        Product_ProductId = c.Int(nullable: false),
                        Customer_CustomerId = c.Int(nullable: false),
                    })
                .PrimaryKey(t => new { t.Product_ProductId, t.Customer_CustomerId })
                .ForeignKey("dbo.Products", t => t.Product_ProductId, cascadeDelete: true)
                .ForeignKey("dbo.Customers", t => t.Customer_CustomerId, cascadeDelete: true)
                .Index(t => t.Product_ProductId)
                .Index(t => t.Customer_CustomerId);
            
        }
        
        public override void Down()
        {
            DropForeignKey("dbo.Branches", "SpecialOffer_SpecialOfferId", "dbo.SpecialOffers");
            DropForeignKey("dbo.ProductCustomers", "Customer_CustomerId", "dbo.Customers");
            DropForeignKey("dbo.ProductCustomers", "Product_ProductId", "dbo.Products");
            DropIndex("dbo.ProductCustomers", new[] { "Customer_CustomerId" });
            DropIndex("dbo.ProductCustomers", new[] { "Product_ProductId" });
            DropIndex("dbo.Branches", new[] { "SpecialOffer_SpecialOfferId" });
            DropTable("dbo.ProductCustomers");
            DropTable("dbo.SpecialOffers");
            DropTable("dbo.Products");
            DropTable("dbo.Customers");
            DropTable("dbo.Branches");
        }
    }
}
