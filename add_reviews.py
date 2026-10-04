import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

reviews_section = """
<section id="reviews" class="rv" style="max-width: 1040px; margin: 60px auto 20px; padding: 0 18px;">
    <div style="text-align:center; margin-bottom: 40px;">
        <h2 style="color: var(--ac); font-size:2.2rem; margin-bottom: 10px;"><i class="fa-brands fa-google" style="color:#4285F4;"></i> Google Reviews</h2>
        <p style="color:var(--mu); font-size:1.1rem;">See what the sangat says about us</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 30px;">
        <!-- Review 1 -->
        <div style="background:#fff; border: 1px solid var(--bd); border-radius:16px; padding:24px; box-shadow:0 4px 15px rgba(0,0,0,0.04);">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                <div style="width:45px; height:45px; border-radius:50%; background:#4285F4; color:#fff; display:flex; align-items:center; justify-content:center; font-size:1.2rem; font-weight:700;">H</div>
                <div>
                    <div style="font-weight:700; color:#333;">Harpreet Singh</div>
                    <div style="color:#facc15; font-size:0.9rem;"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                </div>
                <i class="fa-brands fa-google" style="margin-left:auto; color:#ccc; font-size:1.5rem;"></i>
            </div>
            <p style="color:#555; font-size:0.95rem; line-height:1.6; margin:0;">"Very peaceful Gurdwara Sahib. The kirtan is always mesmerising and the community is very welcoming. Langar sewa is exceptionally well organized."</p>
        </div>
        
        <!-- Review 2 -->
        <div style="background:#fff; border: 1px solid var(--bd); border-radius:16px; padding:24px; box-shadow:0 4px 15px rgba(0,0,0,0.04);">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                <div style="width:45px; height:45px; border-radius:50%; background:#0F9D58; color:#fff; display:flex; align-items:center; justify-content:center; font-size:1.2rem; font-weight:700;">M</div>
                <div>
                    <div style="font-weight:700; color:#333;">Manjit Kaur</div>
                    <div style="color:#facc15; font-size:0.9rem;"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                </div>
                <i class="fa-brands fa-google" style="margin-left:auto; color:#ccc; font-size:1.5rem;"></i>
            </div>
            <p style="color:#555; font-size:0.95rem; line-height:1.6; margin:0;">"Great place to connect with Sangat. They also hold regular Gurbani and Punjabi classes for kids which is a wonderful initiative for the coming generation."</p>
        </div>
        
        <!-- Review 3 -->
        <div style="background:#fff; border: 1px solid var(--bd); border-radius:16px; padding:24px; box-shadow:0 4px 15px rgba(0,0,0,0.04);">
            <div style="display:flex; align-items:center; gap:12px; margin-bottom:16px;">
                <div style="width:45px; height:45px; border-radius:50%; background:#DB4437; color:#fff; display:flex; align-items:center; justify-content:center; font-size:1.2rem; font-weight:700;">J</div>
                <div>
                    <div style="font-weight:700; color:#333;">Jaswinder</div>
                    <div style="color:#facc15; font-size:0.9rem;"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
                </div>
                <i class="fa-brands fa-google" style="margin-left:auto; color:#ccc; font-size:1.5rem;"></i>
            </div>
            <p style="color:#555; font-size:0.95rem; line-height:1.6; margin:0;">"Beautiful ambiance and highly disciplined environment. The Nagar Kirtan arrangements are always top notch. Truly blessed to be part of this Society."</p>
        </div>
    </div>
    
    <div style="text-align:center;">
        <a class="btn" target="_blank" rel="noopener" href="https://www.google.com/maps?q=Dustdaman+Sikh+Society,+12899+76+Ave,+Surrey,+BC+V3W+1E6" style="background:#fff; color:#4285F4; border: 2px solid #4285F4;"><i class="fa-solid fa-pen-to-square"></i> Leave a Review on Google</a>
    </div>
</section>
"""

html = html.replace('<section id="location"', reviews_section + '\n<section id="location"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
