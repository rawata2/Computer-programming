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
    public class SpecialOffersController : ApiController
    {
        private PowerContext db = new PowerContext();

        // GET: api/SpecialOffers
        public IQueryable<SpecialOffer> GetSpecialOffers()
        {
            return db.SpecialOffers;
        }

        // GET: api/SpecialOffers/5
        [ResponseType(typeof(SpecialOffer))]
        public async Task<IHttpActionResult> GetSpecialOffer(int id)
        {
            SpecialOffer specialOffer = await db.SpecialOffers.FindAsync(id);
            if (specialOffer == null)
            {
                return NotFound();
            }

            return Ok(specialOffer);
        }

        // PUT: api/SpecialOffers/5
        [ResponseType(typeof(void))]
        public async Task<IHttpActionResult> PutSpecialOffer(int id, SpecialOffer specialOffer)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            if (id != specialOffer.SpecialOfferId)
            {
                return BadRequest();
            }

            db.Entry(specialOffer).State = EntityState.Modified;

            try
            {
                await db.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!SpecialOfferExists(id))
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

        // POST: api/SpecialOffers
        [ResponseType(typeof(SpecialOffer))]
        public async Task<IHttpActionResult> PostSpecialOffer(SpecialOffer specialOffer)
        {
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            db.SpecialOffers.Add(specialOffer);
            await db.SaveChangesAsync();

            return CreatedAtRoute("DefaultApi", new { id = specialOffer.SpecialOfferId }, specialOffer);
        }

        // DELETE: api/SpecialOffers/5
        [ResponseType(typeof(SpecialOffer))]
        public async Task<IHttpActionResult> DeleteSpecialOffer(int id)
        {
            SpecialOffer specialOffer = await db.SpecialOffers.FindAsync(id);
            if (specialOffer == null)
            {
                return NotFound();
            }

            db.SpecialOffers.Remove(specialOffer);
            await db.SaveChangesAsync();

            return Ok(specialOffer);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                db.Dispose();
            }
            base.Dispose(disposing);
        }

        private bool SpecialOfferExists(int id)
        {
            return db.SpecialOffers.Count(e => e.SpecialOfferId == id) > 0;
        }
    }
}