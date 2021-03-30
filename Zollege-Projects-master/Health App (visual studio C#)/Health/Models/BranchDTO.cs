using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Health.Models
{
    public class BranchDTO
    {
        public int BranchId { get; set; }


        public string Name { get; set; }
        public string Location { get; set; }
        public DateTime Established { get; set; }

        public List<ProductDTO> Products { get; set; }
    }
}