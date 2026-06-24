# Theme Weights — Rokugan / L5R 5E   (hook: themes; FIXED for the whole campaign)

> **Operative digest:** Each new adventure rolls its 5 Theme priorities from these drama weights
> (`adventure_crafter.py themes --style drama --campaign <dir>` → saved to adventure.json). Themes bias every
> Turning Point; honor the rolled order — don't reorder them to steer the story.

# Every adventure rolls its 5 Theme priorities from these weights (adventure_crafter.py themes).
# Samurai drama: the giri/ninjō heart (Personal) and the court (Social) lead; honor & the
# spirit-dark keep Tension high; mysteries of blood, omen, and scheme recur; violence is decisive
# but not the default register.
Personal: 3      # giri vs ninjō, duty, belonging, the bonds that cost
Social: 3        # court, face, clan politics, intrigue
Tension: 2       # honor at stake, the supernatural, looming consequence
Mystery: 2       # secrets, omens, schemes, hidden blood
Action: 1        # the four conflicts strike hard when they come
# Optional fixed First-Priority theme (the genre's spine): the duty-vs-desire axis ->
first_priority: Personal
