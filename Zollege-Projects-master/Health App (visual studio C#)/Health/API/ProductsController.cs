using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.Entity.Infrastructure;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Web.Http;
using System.Web.Http.Description;
using Health.Models;

namespace Health.API
{
    public class ProductsController : ApiController
    {
        private PowerContext db = new PowerContext();
       

        // GET: api/Products
        public IQueryable<ProductDTO> GetProducts()

        {
            var products = from product in db.Products
                           select new ProductDTO()
                           {
                               ProductId = product.ProductId,
                               Name = product.Name,
                               PriceInEuro = product.PriceInEuro,
                               Description = product.Description,
                               Size = product.Size,
                               Customers = product.Customers.Select(customer => new CustomerDTO()
                               {
                                   CustomerId = customer.CustomerId,
                                   Name = customer.Name,
                                   PhoneNumber = customer.PhoneNumber,
                                   Gender = customer.Gender,
                                   AgeInYears = customer.AgeInYears,
                               }
                                                           ).ToList()

                           };

            return products;
        }

        // GET: api/Products/5
        [ResponseType(typeof(Product))]
        public async Task<IHttpActionResult> GetProduct(int id)
        {
            Product product = await db.Products.FindAsync(id);
            if (product == null)
            {
                return NotFound();
            }
            ProductDTO products = new ProductDTO
            {
                ProductId = product.ProductId,
                Name = product.Name,
                PriceInEuro = product.PriceInEuro,
                Description = product.Description,
                Size = product.Size,
                Customers = product.Customers.Select(a => new CustomerDTO()
                {
                    CustomerId = a.CustomerId,
                    Name = a.Name,
                    PhoneNumber = a.PhoneNumber,
                    Gender = a.Gender,
                    AgeInYears = a.AgeInYears,

                }
                                 ).ToList()
            };

            return Ok(product);
        } 
        
    

        // PUT: api/Products/5
        [ResponseType(typeof(void))]
        public async Task<IHttpActionResult> PutProduct(int id, Product product)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            if (id != product.ProductId)
            {
                return BadRequest();
            }

            db.Entry(product).State = EntityState.Modified;

            try
            {
                await db.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!ProductExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return StatusCode(HttpStatusCode.NoContent);
        }

        // POST: api/Products
        [ResponseType(typeof(Product))]
        public async Task<IHttpActionResult> PostProduct(Product product)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            db.Products.Add(product);
            await db.SaveChangesAsync();

            return CreatedAtRoute("DefaultApi", new { id = product.ProductId }, product);
        }

        // DELETE: api/Products/5
        [ResponseType(typeof(Product))]
        public async Task<IHttpActionResult> DeleteProduct(int id)
        {
            Product product = await db.Products.FindAsync(id);
            if (product == null)
            {
                return NotFound();
            }

            db.Products.Remove(product);
            await db.SaveChangesAsync();

            return Ok(product);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        private bool ProductExists(int id)
        {
            return db.Products.Count(e => e.ProductId == id) > 0;
        }
    }
}