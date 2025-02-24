
 
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
            
    def sayHello(self):
        print("hi")
        
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
        |   frame_m_cost(float)  : Meter price for the frame bar unit         |
        |   frame_len (float)    : Length of frame leistung used              |
        |   coverage (float)     : number between 0 and 1. Expresses how      |
        |                          much of the painting is detailed           |
        |                          painting work,e.g. the customer is not     |
        |                          charged for a solid color background.      |
        |   name (str)           : Name of the painting                       |
        |_____________________________________________________________________|
        """    
        canvas_cost    = kwargs.get("canvas_cost", 0)                          # [DKK]
        frame_m_cost   = kwargs.get("frame_m_cost", 0)                         # [DKK/m]
        frame_len      = kwargs.get("frame_len", 0)                            # [m]
        coverage       = kwargs.get("coverage", 1)                           
        name           = kwargs.get("name", "")
        
        area           = w*h                                                   # [cm^2]
        effective_area = area*coverage                                         # [cm^2]
        paint_cost     = effective_area*self.paint_pr_cm2                      # [DKK]
        artistic_price = effective_area*self.artistic_pr_cm2                   # [DKK]
        
        frame_cost     = frame_m_cost * frame_len                              # [DKK]
        
        material_cost  = canvas_cost + frame_cost + paint_cost                 # [DKK]
        
        price_dkk      = int(artistic_price + material_cost)                   # [DKK]
        
        price_eur      = int(price_dkk * self.DKK2EUR)                         # [EUR]
    
        print(f"Price for painting: '{name}' is {price_dkk} DKK or {price_eur}€")
    
        
if __name__ == "__main__":
    p = PaintingPricer()
    
    p.calculate_price(15, 15, coverage=0.95, name="Bird Painting", 
                      frame_len=1.5, frame_m_cost=50, canvas_cost=80)
    
    p.calculate_price(70, 50, coverage=0.5, name="Sara", 
                      frame_len=2.5, frame_m_cost=50, canvas_cost=100)   
    
    p.calculate_price(100, 60, coverage=0.6, name="Aarhus Sunrise", 
                     frame_len=3.2, frame_m_cost=50, canvas_cost=200)   
   