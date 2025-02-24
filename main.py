
 
class PaintingPricer:
    """
    ===========================================================================
    || Class for calculating painting prices                                 ||
    ===========================================================================
    """
    def __init__(self, **kwargs):      
        self.paint_pr_cm2    = kwargs.get("paint_pr_cm2", 2)                   # [DKK] Average price of paints pr. square centimeter
        self.artistic_pr_cm2 = kwargs.get("artistic_pr_cm2", 0.5)              # "Artistic price" - how much is the artistic value/skill value?
        
        self.DKK2EUR = 0.13                                                    # DKK to EUR Currency Exchange Rate
        self.DKK2USD = 0.14                                                    # DKK to USD Currency Exchange Rate  
        
    def calculate_price(self, w, h, **kwargs):
        """
        -----------------------------------------------------------------------
        | Calculates the price of the painting based on width, height and     |
        | a few other variables.                                              |
        -----------------------------------------------------------------------
        | INPUT:                                                              |
        |   w (float)            : Width of the painting                      |
        |   h (float)            : Height of the painting                     |
        |   canvas_cost (float)  : Cost of the blank canvas                   |
        |   frame_m_cost(float)  : Meter price for the frame bar unit [DKK/m] |
        |   frame_len (float)    : Length of frame bar used [m]               |
        |   coverage (float)     : number between 0 and 1. Expresses how      |
        |                          much of the painting is detailed           |
        |                          painting work,e.g. the customer is not     |
        |                          charged for a solid color background.      |
        |   name (str)           : Name of the painting                       |
        |_____________________________________________________________________|
        """    
        self.w            = w
        self.h            = h
        self.canvas_cost  = kwargs.get("canvas_cost", 0)                       # [DKK]
        self.frame_m_cost = kwargs.get("frame_m_cost", 0)                      # [DKK/m]
        self.frame_len    = kwargs.get("frame_len", 0)                         # [m]
        self.coverage     = kwargs.get("coverage", 1)                           
        self.name         = kwargs.get("name", "")
        self.post         = kwargs.get("post", False)
        
        self.post_costs   = 0
        
        self._calc_price()
        
        if self.post:
            self.estimate_postage_costs()
        
    def _calc_price(self):

        area           = self.w*self.h                                         # [cm^2]
        effective_area = area*self.coverage                                    # [cm^2]
        paint_cost     = effective_area*self.paint_pr_cm2                      # [DKK]
        artistic_price = effective_area*self.artistic_pr_cm2                   # [DKK]
        
        frame_cost     = self.frame_m_cost * self.frame_len                    # [DKK]
        
        material_cost  = self.canvas_cost + frame_cost + paint_cost            # [DKK]
        
        self.price_dkk = int(artistic_price + material_cost)                   # [DKK]  
        self.price_eur = int(self.price_dkk * self.DKK2EUR)                    # [EUR]
        self.price_usd = int(self.price_dkk * self.DKK2USD)                    # [USD]
        
    def print_result(self, currency="DKK"):
        
        if currency == "DKK":
            print(f"Price for painting: '{self.name}' is {self.price_dkk} DKK")
            if self.post: print(f"Price for postage: {self.post_dkk} DKK")
        elif currency == "USD":
             print(f"Price for painting: '{self.name}' is ${self.price_usd}")
             if self.post: print(f"Price for postage: ${self.post_usd}")
        elif currency == "EUR":
             print(f"Price for painting: '{self.name}' is {self.price_eur}$")
             if self.post: print(f"Price for postage: ${self.post_eur}€")
    
 
    def estimate_postage_costs(self, destination="Denmark"):
        """
        A rough estimation of postage costs
        Source https://www.postnord.dk/siteassets/pdf/priser/2025/postpakker-2025-01-01.pdf
        """
        if destination == "Denmark":
            self.post_dkk = 100                                              # [DKK] 
 
        self.post_eur = int(self.post_dkk * self.DKK2EUR)                    # [EUR]
        self.post_usd = int(self.post_dkk * self.DKK2USD)                    # [USD]
        
        
if __name__ == "__main__":
    
    p = PaintingPricer() 
    p.calculate_price(70, 50, coverage=0.5, name="Girl with earring", 
                      frame_len=2.5, frame_m_cost=50, canvas_cost=100, post=True)   
    p.print_result("USD")
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 