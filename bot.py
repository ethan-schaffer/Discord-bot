# -*- coding: utf-8 -*-
import discord

with open('token.txt') as token_file:
    for line in token_file:
        login_token = line

rules = []
awards = []
definition_list = []
definition_list.append(("Alliance", """A grouping of two Teams that work together for a given Match. Alliances are designated as
either \"Red\" or \"Blue."""))
definition_list.append(("Alliance Station", """The designated \"Red\" or \"Blue\" Alliance Area adjacent to the Playing Field where the
Drivers and Coach stand or move within during a Match. Station One is the Alliance Station closest to the
audience."""))
definition_list.append(("Area", """The space defined by the vertical projection of the outside edge of a region’s boundary (for example,
gaffers tape, goal, Playing Field Wall). The boundary element (tape, wall, markings, etc.) is considered to be
part of the Area for the purposes of determining Inside and Outside."""))
definition_list.append(("Autonomous Period", """A thirty-second period in which the Robots operate and react only to sensor inputs
and to commands pre-programmed by the Team onto the onboard Robot control system. Human control of
the Robot is not permitted during this time."""))
definition_list.append(("Balanced", """The condition where a Robot is Completely Supported by a single Balancing Stone and no outer
edge of the Balancing Stone is Supported by the Playing Field Floor, Robot parts, or Game Elements."""))
definition_list.append(("Balancing Stone", """A 23 inches (58.4 cm) x 23 inches (58.4 cm) surface located approximately 2 inches (5.08 cm) 
above the Playing Field Floor. The Balancing Stone surface is Supported by a 
5.75 inches (14.6cm) x 5.75 inches (14.6 cm) x 1.375 inch (3.5 cm) tall pylon."""))
definition_list.append(("Block / Blocking", """Preventing an opposing Alliance Robot from accessing an Area or Alliance-specific
Game Element for an extended period by obstructing ALL paths of travel to the object or Area. Active
defense played by a Robot shadowing an opposing Alliance Robot that effectively eliminates all paths of
travel between the opposing Alliance Robot and an Area or Alliance-specific Game Element is considered
Blocking, even though at any frozen point in time there is an open path. See also Trap / Trapping (which
may be considered the same except it is FROM a Game Element or Area of the Playing Field)."""))
definition_list.append(("Cipher", """ The Cipher is a pattern of twelve (12) brown and gray Glyphs Scored into a Cryptobox. There are
six (6) Ciphers (see Appendix E) that if completed by an Alliance will earn that Alliance points and the ability
to Score a Relic prior to the End Game."""))
definition_list.append(("Coach", """ A student Team member or adult mentor designated as the Drive Team advisor during the Match
and identified by wearing a \"Coach\" badge or identifying marker."""))
definition_list.append(("Column", """ There are three (3) Columns per Cryptobox; Left, Center, and Right. A Column is Scored when
there are four (4) Scored Glyphs in the Column and there is a Scored Glyph in each of the four (4) Rows
that make up that Column."""))
definition_list.append(("Competition Area", """ The Area where all the Playing Fields, Alliance Stations, scoring tables, on-deck
queuing tables, event officials, and other tournament items relating to Match play are located. The Team Pit
Area and practice Playing Fields are not part of the Competition Area."""))
definition_list.append(("Control / Controlling", """An object is considered to be Controlled by a Robot if the object is following the
movement of the Robot. Objects that are Controlled by a Robot are considered to be part of the Robot. See
Possess / Possessing to learn about a related term. Examples include, but are not limited to:
• Carrying:  holding Game Elements Inside or Outside of a Robot."
• Herding: pushing or impelling Game Elements to a desired location or direction that gains a
strategic advantage beyond moving the Robot around the field.
• Holding: Trapping one or more Scoring Elements against a Game Element, Playing Field Wall, or
Robot in an attempt to shield or guard them.
• Launching: propelling Game Elements into the air or throwing in a forceful way.
Examples of interaction with Game Elements that are not Controlled include, but are not limited to:
• Plowing: Inadvertent contact with Game Elements while in the path of the Robot moving about the
Playing Field.
• Deflecting: Inadvertent contact with a launched Game Element as it bounces off a Robot.
Cryptobox: An Alliance-specific Scoring Area where Robots place Glyphs. Each Cryptobox contains three
(3) vertical Columns and four (4) horizontal Rows. There are four (4) Alliance-specific Cryptoboxes (2 red, 2
blue)."""))
definition_list.append(("Cryptobox Key",
                    """ A randomly selected Cryptobox Column used as a Scoring achievement during the Autonomous Period."""))
definition_list.append(("Disable / Disabled", """A Robot that is no longer active for the remainder of the Match due to a Robot failure
or by the request of a referee. Teams may not Disable a Robot without the permission of a Field Technical
Advisor or referee. If a referee Disables a Robot during a Match, he/she will ask the Team to drive their
Robot to a neutral position on the Playing Field, issue a stop command with the Driver Station, and place
their Driver Station in a hands-off location on a tournament-provided structure or the Alliance Station floor."""))
definition_list.append(("Disqualified / Disqualification / Disqualify",
                    """A Team that is Disqualified from a Match has their Robot Disabled and will not receive credit for the Match(i.e., no Qualifying or Ranking points)"""))
definition_list.append(("Drive Team",
                    """Up to three representatives (two Drivers and one Coach) from the same Team."""))
definition_list.append(("Driver", """A pre-college student Team member responsible for operating and controlling the Robot and
identified by wearing a tournament supplied \"Driver\" badge or identifying marker."""))
definition_list.append(
    ("Driver-Controlled Period", """The two-minute time period in which the Drivers operate the Robots."""))
definition_list.append(("Driver Station", """Hardware and software used by a Drive Team to control their Robot during a Match.The
Driver Station consists of an Android device, FIRST Tech Challenge supplied Android App, adapter
cable(s), optional non-powered (i.e., does not draw power from a DC power input port) USB Hub, an
optional commercial off the shelf USB external battery connected to the USB Hub to charge the Android
device at any time, and up to two controllers to drive the Robot.The only allowed controller models are the
Logitech F310 Gamepad and the Xbox 360 Controller for Windows (Part  #: 52A-00004)."""))
definition_list.append(("End Game", """The last thirty seconds of the Driver-Controlled Period."""))
definition_list.append(("Game Element", """Any item Robots interact with to play the game.Game Elements for this year’s game include: Glyphs, Relics, Jewels, Balancing Stones, Relic Recovery Zones, Pictographs, and the Cryptoboxes."""))
definition_list.append(("Glyph", """ An Alliance neutral Scoring Element for the game. The Glyph is a foam cube measuring
approximately 6 inches ± 0.125 inches (15.2 cm ± 0.3) on a side. Brown Glyphs weigh approximately 4.18
ounces (118.39 gm) and gray Glyphs weigh approximately 3.83 ounces (108.64 gm). There are twenty-four
(24) gray Glyphs and twenty-four (24) brown Glyphs."""))
definition_list.append(("Glyph Scoring", """ A Glyph is considered Scored when any part of the Glyph is between two Cryptobox Rails
and is not in contact with a Robot of the corresponding Alliance. A 2 inch wide strip of tape is placed on the
Playing Field Floor across the tips of the Rails to provide a visual aid to help determine if a Glyph is between
the Rails. See Appendices C and D for further detail."""))
definition_list.append(("Glyph Pit", """ The location where forty-four (44) Glyphs reside at the start of a Match (there are an additional
four (4) Glyphs Pre-loaded into the Robots). The Glyphs are randomly placed into the Glyph Pit."""))
definition_list.append(("In (Inside) / Completely In (Completely Inside)", """An object that has crossed into the upwards vertical (i.e.,
at a right angle to the Playing Field Floor) extension of a defined Area’s boundary is Inside the Area. An
object that is entirely within the upwards vertical extension of a defined Area’s boundary is Completely
Inside the Area. The boundary element (tape, wall, markings, etc.) is part of the Area for the purposes of
determining Inside and Outside."""))
definition_list.append(("Inadvertent", """ An outcome that is not a planned strategy and not the predictable result of persistent or
repeated actions."""))
definition_list.append(("Inconsequential", """ An outcome that does not influence Scoring or gameplay."""))
definition_list.append(("Jewel", """ An object that Robots interact with during the Autonomous Period to earn points for their Alliance.
FIRST® RELIC RECOVERY℠ is played with four (4) Jewel Sets which are located as shown in Figure 1.3-1.
There are four (4) Jewels per Alliance. The Platform is a 0.48 inches (1.2 cm) thick plate with two holes into
which the Jewels are placed. The Platforms are not affixed to the Playing Field in any manner. The Jewels
measure 3.75 inches (9.5 cm) in diameter and weigh approximately 1.98 ounces (56.13 gm)."""))
definition_list.append(("Jewel Set", """ Jewel Set consists of a platform and two Jewels. Each Jewel Set starts the Match with two
Jewels, one red, one blue."""))
definition_list.append(("Match", """ A head-to-head competition between two Alliances. A Match consists of a thirty-second
Autonomous Period followed by a two-minute Driver-Controlled Period for a total time of two minutes and
thirty seconds."""))
definition_list.append(("Off / Completely Off", """ Not physically in contact with or Supported by an object, surface, etc."""))
definition_list.append(("On / Completely On", """ An object that is physically in contact with and at least partially Supported by an
object, surface, etc. is considered On. An object that is entirely Supported by another object, surface, etc. is
Completely On."""))
definition_list.append(("Out / Outside", """ An object that has NOT crossed into any part of a defined Area is Outside the Area."""))
definition_list.append(("Park / Parked", """ The condition where a Robot is motionless."""))
definition_list.append(("Penalty", """ The consequence imposed for a rule or procedure violation that is identified by a referee. When a
Penalty occurs, points will be awarded to the Alliance that did not incur the Penalty. Penalties are further
defined into Minor Penalties (ten points) and Major Penalties (forty points). Penalties may also escalate to
issuing of a Yellow Card or Red Card as a result of a continued occurrence of a rule violation and upon
discretion of the Referee."""))
definition_list.append(("Yellow Cards and Red Cards", """In addition to rule violations explicitly listed in section 1.6, Yellow
Cards and Red Cards are used in the FIRST Tech Challenge to manage Team and Robot behavior
that does not align with the mission of FIRST.
    The Head Referee may assign a Yellow Card as a warning, or a Red Card for Disqualification in a
Match, as a result of egregious Robot or Team member behavior, or repeated (3 or more) violations 
of a rule at the event. A Yellow Card or Red Card is indicated at the end of a Match by the Head
Referee standing in front of the Team’s Alliance Station and holding a Yellow Card and/or Red Card
in the air.
    Yellow Cards are additive, meaning that a second Yellow Card is automatically converted to a Red
Card. A Team is issued a Red Card for any subsequent incident in which they receive an additional
Yellow Card, including earning a second Yellow Card during a single match. To issue the second
yellow card, the Head Referee will stand in front of the Team’s Alliance Station and hold a Yellow Card
and Red Card. The Head Referee will signal the second Yellow Card after the match has ended.
A Team that has received either a Yellow Card or a Red Card carries a Yellow Card into following
matches, except as noted below. A Red Card results in match Disqualification. Multiple Red Cards
may lead to Tournament Disqualification. Once a Team receives a Yellow Card or Red Card, the
Team number is presented with a yellow background on the audience screen at the beginning of all
following matches. This is a reminder to the Team, referees, and audience the Team carries a
Yellow Card.
    Yellow Cards do not carry over from the qualification Matches to the elimination Matches. During the
elimination Matches, Yellow and Red Cards count against the entire Alliance, not to a specific Team.
If a Team receives a Yellow Card or Red Card, it results in the entire Alliance receiving the Yellow
Card or Red Card for that Match. If two different Teams on the same Alliance are issued Yellow
Cards, the entire Alliance is issued a Red Card. A Red Card results in zero (0) points for that Match,
and the Alliance loses the Match. If both Alliances receive Red Cards, the Alliance which committed
the action earning the Red Card first chronologically loses the Match."""))
definition_list.append(("Pictograph", """ An image containing an encoded message that reveals the location of the Cryptobox Key.
The Pictograph is attached to the Playing Field Wall adjacent to each Jewel platform. There are three
different Pictographs, each representing a different Column in the Cryptobox. The Pictograph is randomly
chosen prior to the start of each Match as described in Appendix G. Pictographs are difficult for humans to
decode; however, a Robot can easily decrypt the Pictograph using its onboard Android phone camera and
the Vuforia software built into the FIRST Tech Challenge software development kit."""))
definition_list.append(("Pin / Pinning", """ Preventing the movement in ALL directions of an opposing Alliance Robot while it is in
contact with the Playing Field Wall, one or more Game Elements, or another Robot."""))
definition_list.append(("Playing Field", """The part of the Competition Area that includes the 12 ft. x 12 ft. (3.66 m x 3.66 m) field, the
Recovery Zone, and all the Game Elements described in the official field documents. From the audience
viewpoint, the Red Alliance Area is on the right side of the Playing Field."""))
definition_list.append(("Playing Field Damage", """A physical change to a Game Element or Playing Field that affects game play or
an action that causes harm to the playability of a Game Element or Playing Field.
For example: Black tire marks on a Game Element is not considered
Playing Field Damage. However, digging a hole larger than 1 inch (2.54
cm) diameter (approximately the size of a US quarter) into the Playing
Field tiles or Glyphs is considered Damage."""))
definition_list.append(("Playing Field Floor", """The surface of the tiles that make up the base of the Playing Field."""))
definition_list.append(("Playing Field Perimeter", """The outside face of the Playing Field Wall."""))
definition_list.append(("Playing Field Wall", """ An approximate 12 inches (0.3m) tall, 12 ft. (3.66 m) long by 12 ft. (3.66 m) wide wall
surrounding the Playing Field Floor. The height of the Wall will vary depending on which Playing Field Wall
is being used at the event. Robots should be built to interact with all legal perimeters."""))
definition_list.append(("Possess / Possessing", """An object is in Possession by a Robot if, as the Robot moves or changes
orientation (for example, moves forward, turns, backs up, spins in place), the object remains in
approximately the same position relative to the Robot. Objects in Possession of a Robot are considered to
be Controlled, and they are part of the Robot. See also Control/Controlling."""))
definition_list.append(("Rail", """The portion of the Cryptobox that extends from the back panel of the Cryptobox onto the field where
Glyphs can be Scored. The color of the Rails indicate which Alliance owns the Cryptobox."""))
definition_list.append(("Recovery Zone", """There are two (2) Alliance-specific Recovery Zone mats that are located outside the
Playing Field Perimeter, adjacent to the wall facing the audience. Each Recovery Zone contains three (3)
distinct Scoring Areas at different distances from the Playing Field Wall where a Robot may place a Relic.
The Scoring Areas are designated as 1, 2, and 3. Recovery Zone 1 is closest to the Playing Field Wall."""))
definition_list.append(("Relic", """ An Alliance-specific Scoring Element. The Relics measure 6.0 inches (15.2 cm) side to side, 3.25
inches (8.25 cm) front to back, and 10 inches (25.4 cm) tall and weigh approximately 4.72 ounces (214 gm)
each. There are four (4) Relics, two (2) per Alliance. At the start of a Match, one Relic is placed in each
corner of the Playing Field Wall, the Relic will be in a standing orientation and must touch both adjacent
walls. The two (2) Blue Relics are adjacent to the wall in front of the Blue Alliance Station and the two (2)
Red Relics are adjacent to the wall in front of the Red Alliance Station."""))
definition_list.append(("Robot", """ Any mechanism that has passed inspection and a Drive Team places on the Playing Field prior to
the start of a Match. A detailed definition of Robot is in the Robot rules section in the Game Manual Part 1."""))
definition_list.append(("Row", """ There are four (4) Rows per Cryptobox. Each Row is delineated by a strip of 1 inch (2.54 cm) wide,
white gaffer tape. The bottom edge of each Row is coincident with the bottom edge of a tape strip. A Row is
Scored when there is a Scored Glyph in each of the three (3) Columns that make up that Row."""))
definition_list.append(("Safe Zone", """ The Area in front of the Cryptobox that is outlined in red or blue gaffer tape. The triangle is 36
inches (91.4 cm) wide at the base and the apex extends 24 inches (61.0 cm) from the wall."""))
definition_list.append(("Scoring / Score", """ Robots earn points for their Alliance by interacting with Scoring Elements and Parking in
specific Areas of the Playing Field. Scoring Elements are considered to be Scored when they are placed in
the appropriate location and are no longer in contact with a Robot from the corresponding Alliance. The
Scoring achievements and their point values are described in section 1.5."""))
definition_list.append(("Scoring Elements", """ Objects that Robots manipulate to earn points for their Alliance. The Scoring Elements
for FIRST® RELIC RECOVERY℠ are Glyphs, Relics, and Jewels."""))
definition_list.append(("Support / Supported / Completely Supported", """A Robot is Supported by an object if that object is bearing
at least some of the weight of the Robot. If the object is bearing all the Robot’s weight, the Robot is
Completely Supported by the object."""))
definition_list.append(("Team", """ Mentors, supporters, and pre-college-aged students affiliated with an entity registered with FIRST
and for the competition."""))
definition_list.append(("Trap / Trapping", """ Preventing an opposing Alliance Robot escaping from a constrained Area of the Playing
Field or from a Game Element for an extended period of time by obstructing ALL paths of travel from the 
object or Area. See also Block / Blocking (which may be considered the same except it is TO a Game
Element or Area of the Playing Field)."""))

awards.append(("inspire", """This judged award is given to the Team that embodied the ‘challenge’ of the FIRST Tech Challenge program.
The Team that receives this award is a strong ambassador for FIRST programs and a role model FIRST Team.
This Team is a top contender for many other judged awards and is a gracious competitor.
The Inspire Award winner is an inspiration to other Teams, acting with Gracious Professionalism® both on and off the Playing Field.
This Team shares their experiences, enthusiasm and knowledge with other Teams, sponsors, their community, and the Judges.
Working as a unit, this Team will have showed success in performing the task of designing and building a Robot.

Required criteria for the Inspire Award:
- The Inspire Award celebrates a Team that, in the opinion of the Judges, is a strong contender in many Award categories. The reliability of the Robot during the Robot competition is one aspect of this Award, but it does not carry more weight than any requirement.
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team is a strong contender for several other Judged awards. The Inspire Award celebrates the strongest qualities of all the Judged Awards.
- The Team is an ambassador for FIRST programs. They demonstrate and document their work in their community.
- Team is positive and inclusive, and each Team member contributes to the success of the Team.
- Team must submit an Engineering Notebook. The Engineering notebook must include an Engineering section, a Team section and a Business or Strategic Plan. The entire Engineering Notebook must be high quality, thoughtful, thorough, detailed and well organized.
- Robot design is creative and innovative, and the Robot performs reliably on the field.
Team communicates clearly about their Robot design and strategy to the judges.
- Team presentation is professional and engaging.
"""))
awards.append(("think", """
**Removing engineering obstacles through creative thinking.**
This judged award is given to the Team that best reflects the journey the Team took as they experienced the engineering design process during the build season.
The Engineering section of the notebook is the key reference for judges to help identify the most deserving Team.
The Team’s Engineering section must focus on the design and build stage of the Team’s Robot.
Journal entries must include descriptions of the underlying science and mathematics of the Robot design and game strategies, the designs, redesigns, successes, and opportunities for improvement.
A Team is not a candidate for this award if they have not completed the Engineering section of the Engineering Notebook.

Required criteria for the Think Award:
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team must submit an Engineering Notebook. The Engineering Notebook must have an Engineering section that includes entries describing underlying science, mathematics, and game strategies.
- The Engineering Notebook must show that the Team has a clear understanding of the engineering design process, with pictures or drawings and details documenting all stages of Robot design.
- Notebook must recount the Team’s journey, experience and lessons learned throughout the season.
- Engineering Notebook must be organized and follow the formatting guidelines provided by FIRST and include a Summary Page.
Note: Teams should review the Engineering Notebook resources published in the Team Management section of the FIRST website.

Strongly suggested criteria for the Think Award:
- Teams should tab or flag 6 to 8 pages of the Engineering section to support entries on the summary page.
"""))
awards.append(("connect", """
**Connecting the dots between community, FIRST, and the diversity of the engineering world.**
This judged award is given to the Team that most connects with their local science, technology, engineering and math (STEM) community.
A true FIRST Team is more than a sum of its parts, and recognizes that engaging their local STEM community plays an essential part in their success.
The recipient of this award is recognized for helping the community understand FIRST, the FIRST Tech Challenge, and the Team itself.
The Team that wins the Connect Award aggressively seeks and recruits engineers and explores the opportunities available in the world of engineering, science and technology.
This Team has a clear Business or Strategic Plan and has identified steps to achieve their goals.

Required criteria for the Connect Award:
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team must submit an Engineering Notebook. The Engineering Notebook must include a Business or Strategic plan that identifies their future goals and the steps they will take to reach those goals.
- The plan could include fund-raising goals, sustainability goals, timelines, outreach, and community service goals.
- Team provides clear examples of developing in person or virtual connections with individuals in the engineering, science, or technology community.
- Team actively engages with the engineering community to help them understand FIRST, the FIRST Tech Challenge, and the Team itself.
"""))
awards.append(("innovate", """
**Bringing great ideas from concept to reality.**

The Rockwell Collins Innovate Award celebrates a Team that thinks outside the box, and has the ingenuity and inventiveness to make their designs come to life.
This judged award is given to the Team that has the most innovative and creative Robot design solution to any specific components in the FIRST Tech Challenge game.
Elements of this award include elegant design, robustness, and ‘out of the box’ thinking related to design.
This award may address the design of the whole Robot, or of a sub-assembly attached to the Robot.
The creative component must work consistently, but a Robot does not have to work all the time during Matches to be
considered for this award.
The Team’s Engineering Notebook must include journal entries to show the design of the component or components and the Team’s Robot to be eligible for this award.
Entries must describe how the Team arrived at their solution.

Required criteria for the Rockwell Collins Innovate Award:
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team must submit an Engineering Notebook. The Engineering Notebook must include an Engineering section that documents the design process and how the Team arrived at their design solution.
- Robot or Robot sub-assembly must be elegant and unique in its design.
- Creative component must be stable, robust, and work reliably.
- Robot design is efficient and consistent with Team plan and strategy.
"""))
awards.append(("design", """
**Industrial design at its best.**

This judged award recognizes design elements of the Robot that are both functional and aesthetic.
The PTC Design Award is presented to Teams that incorporate industrial design elements into their solution.
These design elements could simplify the Robot’s appearance by giving it a clean look, be decorative in nature, or
otherwise express the creativity of the Team.
The winning design should not compromise the practical operation of the Robot but complement its purpose.
This award is sponsored by Parametric Technology Corporation (PTC), developers of the CAD tools, Creo and Mathcad.
PTC gives licenses to the FIRST Tech Challenge Teams for these software products to help them with their designs.

Required criteria for the PTC Design Award:
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team must submit an Engineering Notebook with an Engineering section that includes detailed Robot design drawings.
- Team demonstrates industrial design principles, striking a balance between form, function, and aesthetics.
- Robot distinguishes itself from others by its aesthetic and functional design.
- Basis for the design is well considered (that is inspiration, function, etc.).
- Use of PTC’s Creo is not required to be eligible; however, Teams that use them in their design are given extra consideration for this award.
"""))
awards.append(("motivate", """
**Sparking others to embrace the culture of FIRST!**

This Team embraces the culture of FIRST and clearly shows what it means to be a Team.
This judged award celebrates the Team that represents the essence of the FIRST Tech Challenge competition through Team building, Team spirit and displayed enthusiasm.
This is a Team who makes a collective effort to make FIRST known throughout their school and community, and sparks others to embrace the culture of FIRST.

Required criteria for the Motivate Award:
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team must submit an Engineering Notebook. The Engineering Notebook must include a Business or Strategic plan that identifies their future goals and the steps they will take to reach those goals. The plan could include fundraising goals, sustainability goals, timelines, outreach, and community service goals.
- The Team is an ambassador for FIRST programs.
- Team can clearly show the successful recruitment of new Teams, mentors, coaches and volunteers who were not already active within the STEM community.
- Team can explain the individual contributions of each Team member, and how these apply to the overall success of the Team.

Strongly suggested criteria for the Motivate Award:
- All Team members take part in their presentation, and actively engage with the judges.
- Team shows a creative approach to materials that market their Team and FIRST.
"""))
awards.append(("control", """
**Mastering Robot intelligence.**

The Control Award celebrates a Team that uses sensors and software to increase the Robot’s functionality on the field.
This award is given to the Team that demonstrates innovative thinking in the control system to solvegame challenges such as autonomous operation, improving mechanical systems with intelligent control, or using sensors to achieve better results on the field.
The control component should work consistently on the field.
The Team’s Engineering Notebook must contain details about the implementation of the software, sensors, and mechanical control.

Required criteria for the Control Award:
- Team shows respect and Gracious Professionalism® to everyone they meet at a FIRST Tech Challenge event.
- Team must apply for the Control Award by filling out the Control Award Content Sheet, located in Appendix D (will be released after September 9, 2017)
- The Team must submit an Engineering Notebook. The Engineering Notebook must include an Engineering section that documents the control components.
- Control Components must enhance the functionality of the Robot on the Playing Field.

Strongly suggested criteria for the Control Award:
- Advanced software techniques and algorithms are encouraged.
- Control Components should work reliably.

The Control award is different from other Awards because Teams must apply for this Award.
A Team applying for this Award must turn in their Control Award Content Sheet to the Judges at the event.
This Award focuses on a Team’s ability to program a Robot that can reliably and efficiently carry out tasks during Match play, in a
way that improves their ability to score during a Match.
A Team can submit their code for Autonomous operation as well as their code for the Driver Controlled operation, if they choose.
The Judges are responsible for collecting the content sheet at the beginning of the Teams’ Interview.
After the Team Interview is complete, the Judges will reference the sections of the Engineering Notebook the Team has
pointed out on the Control Award Content Sheet.

The Judges should pay attention to look for:
- What sensors and hardware the Team has tried on the Robot;  what worked, what didn’t, and why.
- Teams are not required to include a printed copy of their Robot code in the Control Award application or in the Engineering Notebook.
- What algorithm or code the Team has programmed  with; what worked, what didn’t, and why.
- The Judges should pay attention to the program and design process. The design process is more critical than the code itself.
- Just like having Engineering Notebook reviewers, the Judge Advisor will assign a group of 2-3 Judges to review the Control Award Content Sheets, once Interviews are complete.
"""))
awards.append(("promote", """
**This judged award is optional and may not be given at all Tournaments.**
Your Judge Advisor will have information about the Judging for this Award.
The Promote Award is given to the Team that is most successful in creating a compelling video message for the public designed to change our culture and celebrate science, technology, engineering and math.
Teams must submit a one-minute long public service announcement (PSA) video based on the PSA subject for the
season.
Teams may win the Promote Award only once at a Championship level event and only once at a qualifying level event.
PSA Subject for 2017-2018 Season: “What I would like the world to know about FIRST”

Required criteria for the Promote Award:
	Video must meet the following criteria:
		- Video Must follow FIRST branding and design standards
		- Video cannot be longer than 60 seconds.
		- Video must be of a high quality, as submissions may be used at a later time to promote
		FIRST.
		- Team must have rights to music used in the video.
		- Music and permissions must be listed in video credits
		- Video must have strong production value.
		- Video must be submitted by the deadline given by the Event Organizer
	- Team must present a thoughtful and impactful video which appeals to the public.
	- Creativity in interpreting the yearly theme is required.
	- Follow video award submission guidelines.
"""))
awards.append(("compass", """
**A beacon and leader in the journey of the FIRST Tech Challenge.**

This judged award is optional and may not be given at all tournaments.
Your Judge Advisor will have information about the Judging for this Award.
The Compass Award recognizes an adult Coach or Mentor who has given outstanding guidance and support to a Team throughout the year, and demonstrates to the Team what it means to be a Gracious Professional.
The winner of the Compass Award will be determined from candidates nominated by FIRST Tech Challenge student Team members, via a 40-60 second video submission.
The video must highlight how their Mentor has helped them become an inspirational Team.
We want to hear what sets the Mentor apart.
Required criteria for the Compass Award:
	Video must meet the following criteria:
		- Video Must follow FIRST branding and design standards
		- Video cannot be longer than 60 seconds.
		- Video must be of a high quality, as submissions may be used at a later time to promote FIRST.
		- Team must have permission from the copyright owners for music used in the video.
		- Music and permissions must be listed in video credits
		- Video must be submitted by the deadline given by the Event Organizer.
	- Video highlights the mentor’s contribution to the Team and demonstrates what sets the mentor apart.
	- Follow video award submission guidelines.
"""))
awards.append(("judges", """
This award is optional and may not be given at all tournaments.
Your Judge Advisor will have information about the Judging for this Award.
During the competition, the judging panel may meet a Team whose unique efforts, performance or dynamics merit recognition, but doesn’t fit into any of the existing award categories.
To recognize these unique Teams, FIRST offers a customizable Judges Award.
The judging panel may select a Team to be honored, as well as the name of the Judges’ Award.
The Judges Award recognizes a Team for their outstanding efforts, but does not factor into the Advancement Criteria.
"""))

rules.append(("RE1", """
Main Power Switch - The Robot Main Power Switch must control all power provided by the Robot main battery pack. FIRST requires Teams to use either the TETRIX (part # W39129), MATRIX (part # 500030), or REV (REV-31-1387) power switch.

This is the safest method for Teams and Field personnel to shut down a Robot.

The Robot main power switch MUST be mounted or positioned to be readily accessible and visible to competition personnel.

A Main Robot Power label must be placed near the Main Power Switch of the Robot.

Attach the image (“POWER BUTTON”) to your Robot near the Main Power Switch.

To be easily seen by field personnel the label should be at least 1 in x 2.63 in (2.54 cm x 6.68 cm, Avery Label # 5160) and placed on a flat surface (not wrapped around corners or cylinders).

The Robot Main Power Switch should be mounted on the Robot so it is protected from Robot-to-Robot contact to avoid inadvertent actuation or damage.
"""))
rules.append(("RE2", """
Battery Mount - Batteries MUST be securely (for example, VELCRO, zip tie, rubber band) attached to the Robot in a location where they will not make direct contact with other Robots or the Playing Field.
"""))
rules.append(("RE3", """
Robot Main Battery – All Robot power is provided by a single 12 V Robot main battery.

The only allowed Robot main power battery packs are:
	a. Core Motor Controller, Core Servo Controller, REV Expansion Hub, Legacy TETRIX DC Motor Controller, and Legacy TETRIX Servo Controller based systems must use one (1) of the following:
		i. TETRIX (W39057, formally 739023) 12 VDC battery pack
		ii. Modern Robotics/MATRIX (14-0014) 12 VDC battery pack
		iii. REV Robotics (REV-31-1302) 12 VDC Slim Battery pack
	b. Legacy MATRIX DC Motor/Servo Controller unified module (i.e., integrated Motor and Servo Controllers) based systems must use one (1) of the following:
		i. Legacy Modern Robotics/MATRIX 9.6 VDC battery pack if the 9.6 VDC Legacy Modern
		Robotics/MATRIX DC Motors are used.
		ii. MATRIX (14-0014) 12 VDC battery pack, TETRIX (W39057, formally 739023) 12 VDC battery
		pack, or REV Robotics (REV-31-1302) 12 VDC Slim Battery pack if TETRIX, AndyMark, REV
		Robotics, or MATRIX 12 VDC Motors are used
	Note: There are similar looking batteries available from multiple sources but the ONLY legal batteries are those listed above.
"""))
rules.append(("RE4", """
Fuses - Where present, fuses must not be replaced with fuses of higher rating than originally installed or according to manufacturer's specifications; fuses may not be shorted out.

Fuses must not exceed the rating of those closer to the battery; if necessary, a fuse may be replaced with a smaller rating.

Fuses must be single use only, self-resetting fuses (breakers) are not allowed.
"""))
rules.append(("RE5", """
Robot Power - Robot power is constrained by the following:
	a. Allowed electronic devices may only be powered by power ports on the Core Power Distribution Module or the REV Expansion Hub except as follows:
		i. The Core Power Distribution Module or REV Expansion Hub is powered by the Robot main battery. If a hybrid of Modern Robotics modules is used with the REV Expansion Hub, the REV Expansion Hub must be powered from a power port on the Core Power Distribution Module.
		ii. Allowed sensors connected to the Core Device Interface Module, the Core Legacy Module, and the REV Expansion Hub.
		iii. Light sources per <RE12>.	
		iv. Video cameras per <RE13>.
	b. The Robot Controller Android device must be powered by its own internal battery or by the built-in charging feature of the REV Expansion Hub; external power is not allowed.
	c. A second REV Expansion Hub is allowed to be connected to and powered by the extra XT30 powerport on a Robot’s first REV Expansion Hub. No other devices are allowed to draw power from the XT30 power ports on a REV Expansion Hub.
"""))
rules.append(("RE6", """
Android Devices - The following Android devices are allowed:
- ZTE Speed
- Motorola Moto G 2nd Generation
- Motorola Moto G 3rd Generation
- Motorola Moto G4 Play
- Google Nexus 5
- Samsung Galaxy S5
	a. No other devices may be used as Robot Controllers or in Driver Stations. See Rule <RS03> for the approved list of Android Operating System versions. Exactly one (1) Android device must be used as the Robot Controller and the USB interface may only connect to the Core Power Distribution Module or a REV Expansion Hub.
	b. Exactly one (1) Android device must be used as a part of the Driver Station.
	c. The Robot Controller Android device must be powered by its own internal battery or by the built-in charging feature of the REV Expansion Hub; external power is not allowed.
	d. The Driver Station Android device must be powered by its own internal battery; external power is allowed from a COTS USB external battery pack that is connected to the allowed USB hub.
"""))
rules.append(("RE7", """
Control Module Quantities - Robot control module quantities are constrained as follows:
	a. Exactly one (1) Core Power Distribution Module is required for Teams using any Modern Robotics Core Control Modules or Legacy MATRIX DC Motor/Servo Controllers.
	b. No more than two (2) Core Device Interface Modules are allowed.
	c. No more than two (2) Core Legacy Modules are allowed.
	d. Any quantity of Core Motor, Legacy TETRIX DC Motor, Core Servo, and Legacy TETRIX Servo Controllers are allowed.
	e. Any quantity of REV Servo Power Modules is allowed.
	f. No more than two (2) REV Expansion Hubs are allowed.
	g. The REV Control Hub is not allowed.
	h. No more than two (2) Legacy MATRIX DC Motor/Servo Controllers (unified module) are allowed.
	"""))
rules.append(("RE8", """
Motor and Servo Controllers - Motor and Servo Controllers are allowed in only one of the following two configurations (cannot mix configurations).
	a. Core Motor Controllers, Core Servo Controllers, REV Expansion Hub, REV Servo Power Module, Legacy TETRIX DC Motor Controllers, and Legacy TETRIX Servo Controllers in any combination.
	b. Legacy MATRIX DC Motor/Servo Controllers (unified module).
"""))
rules.append(("RE9", """
DC Motors – A maximum of eight (8) DC motors are allowed. The only allowed motors are as follows:
a. Core Motor Controller, REV Expansion Hub, and Legacy TETRIX DC Motor Controller based systems must use the following 12 VDC motors in any combination.
	i. TETRIX 12V DC Motor
	ii. AndyMark NeveRest series 12V DC Motors
	iii. Modern Robotics/MATRIX 12V DC Motors
	iv. REV Robotics HD Hex 12V DC Motor
	v. REV Robotics Core Hex 12V DC Motor
b. Legacy MATRIX DC Motor/Servo Controller based systems powered by a 12 VDC Battery must use the following 12 VDC motors in any combination.
	i. TETRIX 12V DC Motor
	ii. AndyMark NeveRest series 12V DC Motors
	iii. Modern Robotics/MATRIX 12V DC Motors
	iv. REV Robotics HD Hex 12V DC Motor
	v. REV Robotics Core Hex 12V DC Motor
c. Legacy MATRIX DC Motor/Servo Controller based systems powered by a 9.6 VDC Battery must only use MATRIX 9.6 VDC motors in any combination. No other DC motors are allowed for use with the Legacy MATRIX DC Motor/Servo Controller.
d. No other DC motors are allowed. The allowed battery, motor controller, and DC motor combinations are summarized in the following table. The check symbol (✓) indicates the DC motor is allowed with the controllers and batteries listed in the rows above it. The “X” symbol is present for DC motors that are not allowed for the listed controller and battery combination.

|Controllers:|Core Motor Controller, REV Expansion Hub, and/or Legacy TETRIX DC Motor Controller|Legacy MATRIX DC Motor/Servo Controller (Unified Module)||
------------|---|----|----
|Batteries:|TETRIX 12 VDC, MATRIX 12 VDC, or REV Robotics 12 VDC|MATRIX 9.6 VDC|TETRIX 12 VDC, MATRIX 12 VDC, or REV Robotics 12 VDC|
|TETRIX 12V|✓|X|✓|
|AndyMark NeveRest Series 12V|✓|X|✓|
|Modern Robotics/MATRIX 12V|✓|X|✓|
|REV HD Hex 12V|✓|X|✓|
|REV Core Hex 12V|✓|X|✓|
|MATRIX 9.6V|X|✓|X|
"""))
rules.append(("RE10", """
Servos – A maximum of twelve (12) servos are allowed. Any servo that is compatible with the attached servo controller is allowed.

Servos may only be controlled and powered by an allowed Servo Controller, REV Expansion Hub or REV Servo Power Module (when used with an allowed Servo Controller or REV Expansion Hub).

Servos may be rotary or linear but are limited to 6V or less and must have the three-wire servo connector.

Teams should be prepared during Robot inspection to show documentation confirming that the servos individually and together on the same servo controller do not exceed the manufacturer specifications for the controller.

Core Servo Controllers and Legacy TETRIX Servo Controllers may control up to two (2) VEX EDR 393 Motors per module.

A VEX Motor Controller 29 must be used between a servo module and each VEX EDR 393 motor.

REV Expansion Hubs must use a REV Servo Power Module between the REV Expansion Hub and the VEX Motor Controller 29.

A maximum of two (2) VEX EDR 393 Motors may be controlled/powered per REV Servo Power Module.

The VEX EDR 393 motor is considered a servo and it is subject to the overall total maximum of twelve (12) servos.
"""))
rules.append(("RE11", """
Sensors - Sensors are subject to the following constraints:
	a. Compatible sensors from any manufacturer may be connected to the Core Device Interface Module or REV Expansion Hub.
	b. Compatible sensors from any manufacturer may be connected to the Logic Level Converter and/or the I2C Sensor Adapter Cable. Refer to Rule <RE14.k> for details on the use of Logic Level Converter and the I2C Sensor Adapter Cable.
	c. Passive electronics may be used as recommended by sensor manufacturers at the interfaces to thesensors.
	d. Voltage sensors are allowed; except on an output port of a motor or servo controller.
	e. Current sensors are allowed; except on an output port of a motor or servo controller.
	f. Simple I2C multiplexers are allowed and they may only be connected to and powered from the I2C connections available on the Core Device Interface Module or the REV Expansion Hub.
	g. Legacy Sensors are allowed and must be directly connected to the Core Legacy Module.
	h. Voltage and/or current sensors are also allowed to connect between the battery pack and the REV Expansion Hub or Core Power Distribution Module.
	i. The HiTechnic Touch Sensor Multiplexor (NTX1060) is allowed.
	j. The HiTechnic Sensor Multiplexor (NSX2020) is not allowed.
"""))
rules.append(("RE12", """
Light Sources - Light sources (including LEDs) are allowed; these may not be focused or directed in any way (for example: lasers and mirrors are not allowed). Approved power sources for lights are as follows:
	a. Internal (as supplied by the manufacturer) battery pack or battery holder
	b. Power ports on the Core Power Distribution Module
	c. Motor-control port on the Core Motor Controller Module
	d. Motor controller port on the Legacy TETRIX DC Motor Controller
	e. REV Expansion Hub:
		i. Motor-control port
		ii. Spare XT30 port
		iii. 5V auxiliary power port
"""))
rules.append(("RE13", """
Video Cameras - Video recording devices (GoPro or similar) are allowed providing they are used only for non-functional post-match viewing and the wireless capability is turned off. Approved video cameras must be powered by an internal (as supplied by the manufacturer) battery.
"""))
rules.append(("RE14", """
Robot Wiring - Robot wiring is constrained as follows:
	a. USB Surge Protectors connected to USB cables are allowed.
	b. Ferrite chokes (beads) on wires and cables are allowed.
	c. Either A Mini USB to OTG (On-The-Go) Micro Cable or a Mini USB adapter and OTG (On-The-Go) Micro Cable is used to connect the Robot Controller Android device to the built-in USB input port of the Core Power Distribution Module or of the REV Expansion Hub.
	d. Non-powered USB hubs connected to the Core Power Distribution Module are allowed.
	e. Anderson PowerPole, and similar crimp or quick connect style connectors are required to connect downstream electronics with the Core Power Distribution Module and are recommended for joining electrical wires throughout the Robot. Power distribution splitters are recommended where appropriate to reduce wiring congestion. All connectors and distribution splitters should be appropriately insulated.
	f. Installed connectors (such as battery-pack connectors, battery charger connectors, and Core Power Distribution Module power input connectors) may be replaced with Anderson PowerPole or any compatible connector.
	g. Power and motor control wires must use consistent color coding with different colors used for the Positive (red, white, brown, or black with a stripe) and Negative/Common (black or blue) wires.
	h. Wire and cable management products of any type are permitted (for example, cable ties, cord clips, sleeving, etc.).
	i. Wire insulation materials of any type are permitted when used to insulate electrical wires or secure motor control wires to motors (for example, electrical tape, heat shrink, etc.).
	j. Power, motor control, servo, encoder, and sensor wires and their connectors may be extended, modified, custom made, or COTS subject to the following constraints:
		i. Power wires are 16 AWG or larger.
		ii. Motor control wires are 22 AWG or larger.
		iii. PWM (servo) wires are 20 AWG or 22 AWG.
		iv. Sensor wires should be the same size or larger than the original wiring.
Teams should be prepared during Robot inspection to show documentation confirming the wire gauges used; particularly for multiconductor cables.
k. Logic Level Converters – Logic Level Converters that are used to connect a REV Expansion Hub to a 5V-compatible I2C sensor or a 5V-compatible digital sensor are allowed. Exactly one Logic Level Converter per I2C device and one Logic Level Converter per digital sensor are allowed. A Logic Level Converter should only draw power from the REV Expansion Hub.
l. Electrically grounding the electronics to the frame of the Robot is not allowed.
"""))
rules.append(("RE15", """
Modifying Electronics - Approved electrical and electronic devices may be modified to make them more usable; they may not be modified internally or in any way that affects their safety.

Examples of modifications that are allowed:
- Shortening or extending wires
- Replacing or adding connectors on wires
- Shortening motor shafts
- Replacing gearboxes and/or changing gears

Examples of modifications that are not allowed:
- Replacing an H-Bridge in a motor controller
- Rewinding a motor
- Replacing a fuse with a higher value than specified by the manufacturer
- Shorting out a fuse
"""))
rules.append(("RE16", """
Driver Station Constraints – Teams provide their own Driver Station and it must comply with the following constraints:
	a. The Driver’s Station must consist only of:
		i. One (1) Android device
		ii. One (1) OTG Cable
		iii. No more than one (1) USB hub
		iv. No more than two (2) gamepads
	b. The Driver Station Android device USB interface may only connect to either:
		i. A Mini USB to OTG (On-The-Go) cable or combination of cables connected to a non-powered USB Hub, or
		ii. One (1) gamepad
	c. One optional COTS USB external battery connected to the USB Hub to charge the Android device is allowed.
	d. The only allowed gamepads are listed below. They may be used in any combination.
		i. Logitech F310 gamepad (Part# 940-00010)
		ii. Xbox 360 Controller for Windows (Part# 52A-00004)
	e. The touch display screen of the Driver Station must be accessible and visible by competition personnel.
Important Note: The Driver Station is a wireless device with a built-in wireless radio. During a match, the Driver Station should not be obscured by metal or other material that could block or absorb the radio signals from the Driver Station.
"""))
rules.append(("RE17", """
Additional Electronics – Electronic devices that are not specifically addressed in the preceding Rules are not allowed.

A partial list of electronics that are not allowed includes: Arduino boards, Raspberry Pi, relays, and custom circuits.
"""))

rules.append(("RM1", """
Allowed Materials - Teams may use raw and post-processed materials to build their Robots, provided they are readily available to the majority of Teams from standard distributors (for example, McMasterCarr, Home Depot, Grainger, AndyMark, TETRIX/PITSCO, MATRIX/Modern Robotics, REV Robotics, etc.).

Examples of allowed raw materials are:
	- Sheet goods
	- Extruded shapes
	- Metals, plastics, wood, rubber, etc.
	- Magnets
Examples of allowed post-processed materials are:
	- Perforated sheet and diamond plate
	- Injection molded parts
	- 3D printed parts
	- Cable, string, rope, filament, etc.
	- Springs of all types: compression, extension, torsion, surgical
	tubing, etc.
"""))
rules.append(("RM2", """
Commercial Off The Shelf Parts - Teams may use Commercial Off The Shelf (COTS) mechanical parts that have a single degree of freedom.

A single degree of freedom is a system whose motion is defined just by a single independent co-ordinate (or function).

It is the intent of FIRST is to encourage Teams to design their own mechanisms rather than purchasing predesigned and pre-manufactured solutions to achieve the game challenge.

Purchased mechanism kits (for example, grippers) that violate the single degree of freedom Rule, either assembled or requiring assembly, are not allowed. COTS drive chassis (for example, AndyMark TileRunner, REV Robotics Build Kit) are allowed provided none of the individual parts violate any otherRules.

Examples of allowed single degree of freedom parts:
	- Linear Slide
	- Single speed (non-shifting) Gearboxes
	- Pulley
	- Lazy Susan
	- Lead Screws
Examples of illegal multiple degrees of freedom parts:
	- Gripper assemblies or kits
	- Ratcheting wrenches
"""))
rules.append(("RM3", """
Holonomic Wheels - Holonomic wheels (omni or mechanum) are allowed.
"""))
rules.append(("RM4", """
3D Printed Parts - 3D printed parts are allowed.
"""))
rules.append(("RM5", """
Modifying Materials and COTS Parts - Allowed materials and legal COTS parts may be modified (that is, drilled, cut, painted, etc.), as long as no other rules are violated.
"""))
rules.append(("RM6", """
Allowed Assembly Methods - Welding, brazing, soldering, and fasteners of any type are legal methods for assembling a Robot.
"""))
rules.append(("RM7", """
Lubricant - Any type of COTS lubricant is allowed, if it doesn’t contaminate the Playing Field, game elements, other Robots, etc.
"""))
rules.append(("RG1", """
Illegal Parts - The following types of mechanisms and parts are not allowed:
	a. Those that could potentially damage the Playing Field and/or Scoring Elements. For example, high traction wheels (for example, AM- 2256) and high grip tread (for example, Rough top) when used in a Robot drive system that may damage the Playing Field are not allowed.
		For example: Black tire marks on an Element is not considered Playing Field damage. However, digging a hole into the Playing Field tiles can be considered damage.
	b. Those that could potentially damage or flip other competing Robots.
	c. Those that contain hazardous materials such as mercury switches, lead, or lead containing compounds, or lithium polymer batteries (except for the Android devices’ internal battery).
	d. Those that pose an unnecessary risk of entanglement.
	e. Those that contain sharp edges or corners.
	f. Those that contain animal-based materials (because of health and safety concerns).
	g. Those that contain liquid or gel materials.
	h. Those that contain materials that would cause a delay of game if released (for example, loose ball bearings, coffee beans, etc.).
	i. Those that are designed to electrically ground the Robot frame to the Playing Field.
	j. Closed gas devices (for example, gas storage vessel, gas spring, compressors, etc.).
	k. Hydraulic devices.
"""))
rules.append(("RG2", """
Maximum Starting Size - The maximum size of the Robot for starting a match is 18 inches (45.72 cm) wide by 18 inches (45.72 cm) long by 18 inches (45.72 cm) high.

The Robot Sizing Box will be used as the official gauge to make sure Robots comply with this Rule.

To pass inspection a Robot must fit within the box while in its match start configuration and orientation without exerting force on the sides or top of the box.

Robots may expand beyond the starting size constraint after the start of the match.

The Alliance flag and preloaded game elements may extend outside the starting volume constraint.

The Robot must be self-supporting while in the Robot Sizing Box by either:
	a. A mechanical means with the Robot in a power-OFF condition. Any restraints used to maintain starting size (that is, zip ties, rubber bands, string, etc.) MUST remain attached to the Robot for the entire match.
	b. A Robot Initialization Routine in the Autonomous operational mode (op mode) program that may preposition the servo motors, with the Robot in a power-ON condition, to the desired stationary position. If the Robot Initialization Routine does move the servos when a program is executed, there must be an indicator on the Robot of this fact. A warning label placed near the Robot’s main power switch is required. Attach the image (“WARNING! - Robot moves on Initialization”) to your Robot near the Robot main power switch if servos are commanded to move during the initialization routine. To be easily seen by field personnel the label should be at least 1 in x 2.63 in (2.54 cm x 6.68 cm, Avery Label # 5160) and placed on a flat surface (not wrapped around corners or cylinders).
"""))
rules.append(("RG3", """
Robot Controller Mount – It is recommended the Robot Controller be accessible and visible by competition personnel. If a Team’s Robot Controller is not accessible and/or visible to competition personnel, the Team may not receive adequate support from the field personnel.

The Robot Controller should be mounted such the display screen is protected from contact with the Playing Field elements and other Robots.

This and other electrical parts (batteries, motor and servo controllers, switches, sensors, wires, etc.) make poor bumpers and are unlikely to survive the rigors of game play when attached in a Robot-to-Robot contact area.

Important Note: The Robot Controller contains a built-in wireless radio that communicates with the Android device in the Driver Station.

In addition to protecting the device from impact, the Robot Controller should not be obscured by metal or other material that could block or absorb the radio signals from the Robot Controller.
"""))
rules.append(("RG4", """
Alliance Flag Holder - Robots MUST include a mounting device to securely hold one Tournament supplied FIRST Tech Challenge Robot Alliance Identification Flag throughout an entire match.

The flag MUST be mounted at the TOP of the Robot and be clearly visible throughout the match to clearly identify a Robot’s Alliance.

Flag posts are typically a soda straw or wooden dowel.

Dimensions of each are close to 0.25 inches (0.635 cm) outer diameter x 0.20 inches (0.5 cm) inner diameter x 8.25 inches (21 cm) length with a triangular flag 4.0 inches (10.16 cm) high x 6.0 inches (15.24 cm) wide.

These may vary from Event to Event; Alliance Flag Holders should be able to securely hold both solid core dowels and open core straws. Mounting devices that damage the flag post are not acceptable.
"""))
rules.append(("RG5", """
Team Number Display - Robots MUST prominently display their Team number (numerals only, for example “12345”) on two separate signs.
	a. The judges, referees, and announcers must be able to easily identify Robots by Team number.
	b. Team number must be visible from at least two opposite sides of the Robot (180 degrees apart).
	c. The numerals must each be at least 2.5 inches (6.35 cm high), at least in 0.5 inches (1.27 cm) stroke
	width, and in a contrasting color from their background. Teams can use Arial Font, Bold, 250 point to
	meet the minimum size requirements.
	d. Team numbers must be robust enough to withstand the rigors of match play. Example robust materials
	include: 1) self-adhesive numbers (that is, mailbox or vinyl numbers) mounted on polycarbonate sheet,
	wood panel, metal plate, etc.; 2) Ink jet or laser printed numbers on paper and laminated.
"""))
rules.append(("RG6", """
Allowed Energy Sources - Energy used by FIRST Tech Challenge Robots, (that is, stored at the start of a match), shall come only from the following sources:
	a. Electrical energy drawn from approved batteries.
	b. A change in the position of the Robot center of gravity.
	c. Storage achieved by deformation of Robot parts. Teams must be careful when incorporating spring-like mechanisms or other items to store energy on their Robot by means of part or material deformation.
"""))
rules.append(("RG7", """
Launching Robot Parts - Parts of the Robot itself may not be launched, even if the part launched is still connected to the Robot by a tether (for example, wire, rope, or cable).
"""))
rules.append(("RG8", """
Launching Game Scoring Elements – Robots are allowed to launch game Scoring Elements through the air unless limited by a game specific Rule.

It is expected that Teams will launch the elements with just enough velocity to score.

If the referees, feel that a Robot is launching Scoring Elements with excessive velocity that would cause a safety issue if they were to leave the field, the Robot will be required to be inspected.

Robots must then demonstrate that a launched Game Element cannot travel in the air more than a distance of 16 ft. (4.88 m) or more than 6 ft. (1.83 m) in elevation.
"""))

rules.append(("T1", """
Egregious behavior by any Team, Team member, or other representative of the Team is not tolerated at a FIRST Tech Challenge Tournament.

Violations of this Rule can result in penalties to the Team, and/or the issuance of a Yellow or Red Card.

Egregious behavior includes, but is not limited to, repeated and/or flagrant violation of gameRules, unsafe behavior or actions, uncivil behavior towards Volunteers, Competition personnel, or Event attendees.
"""))
rules.append(("T2", """
Yellow Cards and Red Cards are used in the FIRST Tech Challenge to manage Team and Robot behavior that does not align with the mission of FIRST. 

Yellow and Red Cards are not limited to just the Competition Area. 

Teams that display egregious behavior in the Pit Area, Judging Rooms, stands, or any other location of the Event can be issued a Yellow or Red Card for egregious behavior. Egregious or repeated (3 or more) Robot or Team member behavior at the Event can result in a Yellow and/or Red Card. The Head Referee may assign a Yellow Card as a warning, or a Red Card for Disqualification in a match. A Yellow Card or Red Card is signaled by the Head Referee standing in front of the Team’s Alliance Station and holding a Yellow Card and/or Red Card in the air. Yellow Cards are additive, meaning that a second Yellow Card is automatically converted to a Red Card. A Team is issued a Red Card for any subsequent incident in which they receive an additional Yellow Card, including earning a second Yellow Card during a single match. To issue the second yellow card, the Head Referee will stand in front of the Team’s Alliance Station and hold a Yellow Card and Red Card. The Head Referee will signal the second Yellow Card after the match has ended. A Team that has received either a Yellow Card or a Red Card carries a Yellow Card into following matches, except as noted below. A Red Card results in match Disqualification. Multiple Red Cards may lead to Tournament Disqualification. Once a Team receives a Yellow Card or Red Card, the Team number is presented with a yellow background on the audience screen at the beginning of all following matches. This is a reminder to the Team, referees, and audience the Team carries a Yellow Card. Yellow Cards do not carry over from the Qualification Matches to the Elimination Matches. During the Elimination Matches, Yellow and Red Cards count against the entire Alliance, not to a specific Team. If a Team receives a Yellow Card or Red Card, it results in the entire Alliance receiving the Yellow Card or Red Card for that match. If two different Teams on the same Alliance are issued Yellow Cards, the entire Alliance is issued a Red Card. A Red Card results in zero (0) points for that match, and the Alliance loses the match. If both Alliances receive Red Cards, the Alliance which committed the action earning the Red Card first chronologically loses the match.
"""))
rules.append(("T3", """
Referees have final game play and scoring authority during the Competition.
Their rulings are final.
	a. The referees will not review any recorded match replays or photographs.
	b. All questions about a m atch or scores must be brought forward to the Referees by using the Referee Question Box located in the Competition Area. Only one student from an Alliance can enter the question box. All questions must be b rought forward within the outlined time:
		i. Qualification Matches: A Team must enter the question box to dispute a Match within the time period of three (3) match es following the disputed Match.
		ii. Elimination Matches and Final Matches: A Team must enter the Referee Question Box to dispute a match before the start of the next match played by the Alliance, regardless if the Team is playing in the next match. The next match played could involve different Alliances. Questions about the last match of the Finals must be brought to the question box no later than 5 minutes after the announcement of the score of the match.
	Students must support their questions by referencing specificRules or posts to the Q&A section of the official FIRST Tech Challenge Forum. Team members must ask their questions in a gracious and respectful manner.
	c. Team members cannot enter the Playing Field for any reason other than to place or retrieve their Robots. Inspection of the Playing Field elements by Team members to determin e scoring is not allowed . Individuals and Teams that violate this Rule will be subject to possible Team penalties that could include m atch disqualifications or even removal from the Tournament.
"""))
rules.append(("T4", """
No Team , Team Member, or Event attendee is allowed to set up their own Wi-Fi 802.11 (2.4GHz or 5GHz) wireless communication in the venue.

Non-allowed wireless communications include, but are not limited to:
	a. Cellular Hot spots ( for example, cell phones, tablets, MiFi).
	b. Ad-hoc networks.
	c. Nintendo DS peer-to-peer.
	d. Bluetooth communication with Robots in the Competition Area.
No Team , Team Member, or Event attendee shall interfere with a Team’ s Wi-Fi Direct® communication with their own Robot.

The Penalty for violating Rule <T4> is disqualification of the entire Team from the Event and their removal from the venue property.

Teams may not ap peal the penalty and no refunds will be given for registration fees, prepaid meals, etc.

FIRST may conduct a post - Event review and decide if any additional penalties are to be imposed on the offending Team.

Teams are encouraged to report wireless security vulnerabilities to the Field Technical Advisor (FTA) at an Event.

Teams should always keep in mind Gracious Professionalism®, and therefore only report valid and verifiable violations of this Rule.

After the Field Technical Advisor is alerted of a potential Rule violation, he or she will confer with the Head Referee.

The Field Technical Advisor and Head Referee will further explore the potential violation of this Rule.

The Head Referee will work with FIRST Headquarters staff to determine if Rule <T4> has been violated, and to disqualify the offending Team.
"""))
rules.append(("T5", """
Wi-Fi Direct® connectivity between the Android devices used as the Robot Controller and the Drivers Station is allowed.

No other wireless communication is allowed.

The Penalty for violating Rule <T5> is disqualification of the entire Team from the Event and their removal from the venue property.

The Head Referee will work with FIRST Headquarters staff to determine if Rule <T5> has been violated, and to disqualify the offending Team.

Teams may not appeal the penalty and no refunds will be given for registration fees, prepaid meals, etc. FIRST may conduct a post-Event review and determine if any additional penalties are to be imposed on the offending Team.
"""))
rules.append(("T6", """
Team members may be asked by the Event Director to use a specific Wi-Fi channel on the Event day.

Teams must comply with the request of the Event Director if asked to use a specific Wi-Fi Channel when supported by an approved Android Device.

Teams that have Android Devices that support channel changing MUST comply with the request of the Event Director to switch their channel before playing in the next match.
"""))
rules.append(("T7", """
Each registered Team may enter only one Robot (a Robot built to play the current season’s game challenge ) into the FIRST Tech Challenge Competition. It is expected that Teams will make changes to their Robot throughout the season and at competitions.
	a. It is against this Rule to compete with one Robot while a second is being adjusted or assembled at a Tournament.
	b. It is against this Rule to switch back and forth between multiple Robots at a Tournament.
	c. It is against this Rule to register and attend concurrent Events with a second Robot. Violations of this Rule will immediately be considered egregious and a deliberate violation of the Rule.
	"""))
rules.append(("T8", """
Only three Team representatives are allowed in the Competition Area; two (2) student drivers, and one (1) coach who are identified by badges labeled ‘driver’ or ‘coach.’ These badges are interchangeable within a Team between matches. Only student Team members wearing a badge labeled as ‘driver’ may drive the Robot during the match. Team representatives beyond the two student drivers and one coach will be asked to leave the Competition Area immediately.
"""))
rules.append(("T9", """
Pre-Match Robot Setup – At the beginning of a match , each Alliance Robot must be set up on the Playing Field in accordance with section 1.5.1 Pre-Match in the Game Manual Part 2. After Robots have been set up on the Playing Field, Drive Teams are required to stand Completely Inside the Alliance Station at the location (Station one or Station two) specified by the Qualification Match schedule.
	a During the Qualification Matches, the Blue Alliance Robots are set up on the Playing Field first , unless the Red Alliance waives their right to set up on the Playing Field second.
	b. During the Elimination Matches, the 3rd and 4th seeded) Alliance Robots are set up on the Playing Field first, unless the higher seeded Alliance waives their right to set up on the Playing Field second. Alliance color doesn’t change the seed ing of a Team during the Elimination Matches. If the 4th seed defeats the 1st seed in the Semi-Finals, they will still have to place their Robot on the field first in the Finals because their seeding will be lower than the 2nd or 3rd seed.
	c. Teams may implicitly waive their right to place their Robots on the Playing Field last by placing their Robot s on the Playing Field before or with the opposing Alliance . There is no need to tell the referees; Teams waive their right by the act of placing their Robots on the Playing Field.
	d. Teams that unnecessarily delay the beginning of a m atch and/or field reset will incur a Minor Penalty for each offense.
Drive Teams are expected to stage their Robots for a match, and remove it from the Playing Field afterwards, safely and swiftly. Drive Team efforts that either intentionally or unintentionally delay the start of a match or the Field reset are not allowed. Examples include, but are not limited to:
	- Late arrival to the Playing Field.
	- Robot maintenance once on the Playing Field
"""))
rules.append(("T10", """
Scores are recorded at the end of the Autonomous Period and Driver - Controlled Period when all objects on the Playing Field have come to rest.

Scores may not be announced to the Teams until some amount of time after the Match has completed.
"""))
rules.append(("T11", """
There are no time-outs during the Qualification Matches.
"""))
rules.append(("T12", """
If no member of the Drive Team is present in the Driver Station at the start of a match , that Team is declared a “no show”. If a Robot cannot report for a match, at least one member of the Drive Team should report to the Playing Field for the m atch.
"""))
rules.append(("T13", """
Teams will receive a minimum of five minutes (5:00) be tween consecutive matches.
"""))
rules.append(("T14", """
During the elimination rounds, each Alliance will be allotted ONE time - out of no more than three minutes (3:00). Time-outs must be called at least two minutes (2:00) before their next m atch ’s starting time. The time-out begins at the time their match was going to start.
"""))
rules.append(("T15", """
All Team members, coaches, and their guests must wear ANSI Z 87.1 certified safety glasses while in the Pit or Competition Area. 

Prescription glasses with ANSI Z 87.1 approved commercial off the shelf side shields are also allowed.

NOTE: FIRST requires all Teams to bring and supply ANSI - approved safety glasses for its Team members, mentors, and guests for each Competition. 

Tinted lenses are allowed as long as Event personnel can see the Volunteer’s, spectator’s, or Team member’s eyes through the safety glasses. 

Sunglasses or deeply shaded safety glasses used in our indoor Event environment are not acceptable.
"""))
rules.append(("T16", """
Skateboards, roller skates, ‘hover boards’, and drones are not allowed at any Tournament. These items can create safety hazards to the Teams, spectators, or Volunteers attending the Event.
"""))
rules.append(("T17", """
No live bands are allowed in the audience or Pit. No loud music, audio systems, whistles, banging sticks, blow horns, etc. are allowed. They prevent Teams from hearing important announcements. Power may be shut off and/or noisemakers confiscated.
"""))
rules.append(("T18", """
Batteries must be charged in an open, well - ventilated area. Drive Teams are expected to stage their Robots for a match , and remove it from the Playing Field afterwards, safely and swift ly. Drive Team efforts that either intentionally or unintentionally delay the start of a match or the Field reset are not allowed. Examples include, but are not limited to: Late arrival to the Playing Field. Robot maintenance once on the Playing Field.
"""))
rules.append(("T19", """
Painting or applying harmful products, sprays, or aerosols are not allowed anywhere in the Tournament. This includes the Pit, Competition, and spectator areas. Note: Teams may apply antistatic spray to their Robot if done outside the venue.
"""))
rules.append(("T20", """
Pit displays may not exceed 10 ft. (3.05 m) x 10 ft. ( 3.05 m) x 10 ft. ( 3.05 m) or a limit specified by the venue, whichever is shorter.
"""))
rules.append(("T21", """
Teams are not allowed to use radios and walkie-talkies anywhere in the venue.
"""))
rules.append(("T22", """
There is no running anywhere during the Event as this is a safety hazard.
"""))
rules.append(("T23", """
Sitting together in a group during Competition matches makes the game more exciting and fun. It allows Team members to show support for their Team. Teams are not allowed to save seating space as there is often not enough seating to hold everyone. Repeated offenses could be considered egregious, and Teams could face consequences for violating this Rule.
"""))
rules.append(("T24", """
Soldering, gluing, brazing, or large power tools are not allowed in the Pit or Competitions Areas unless the Event Director specifically allows them.
"""))
rules.append(("T25", """
Because of siteRules or contracts, FIRST cannot allow Teams or individuals to sell items, such as T-shirts, pins, etc., at any Events. Fundraising for a cause is allowed with consent of the Tournament Director; fundraising for a Team is not allowed.
"""))
rules.append(("T26", """
Check with the Tournament Director before bringing food to an Event, as some venues will not allow outside food on-site because of contracts and agreements.
"""))
rules.append(("T27", """
Open-toed or open-backed shoes are not allowed in the Pit Area or in the Competition Area.
"""))

rules.append(("S1","""safe Robot and Playing Field Damage – If at any time the Robot operation is deemed unsafe or has damaged the Playing Field or another Robot, by the determination of the referees, the offending Robot may be Disabled and the Team may be issued a Yellow Card. Re-inspection of the Robot is required before it may play another Match.
The intent of this rule is to immediately stop unsafe Robot actions or Playing Field Damage that is likely to persist with continued Robot operation. Robots that can continue safe operation without damaging the Playing Field will receive a warning and may continue to play the Match. Robots will be Disabled for unsafe operation or Playing Field Damage that occurs after the first warning for the tournament."""))

rules.append(("S2","""Robot Extension Outside the Playing Field Perimeter – If any portion of the Robot contacts anything Outside the Playing Field Perimeter, the Team will be issued a Yellow Card and it may be Disabled immediately for the remainder of the Match, unless allowed by Game-Specific rule(s) listed in Section 1.6.3. See the game definitions in section 1.4 for a complete description of the Playing Field Perimeter. The intent of this rule is not to Penalize an Alliance for Inadvertent, safe Robot extension Outside the Playing Field Perimeter. Intentional Robot extension Outside the Playing Field is not permitted, except as allowed by game-specific rules listed in Section 1.6.3."""))

rules.append(("S3",""" Safety Gear – All members of the Drive Team are required to wear approved eye protection and shoes with closed-toes and a closed-back. If any member of the Drive Team is not wearing these safety items, the referee will issue a warning and if the situation is not remedied within thirty seconds, the offending member(s) of the Drive Team must leave the Competition Area for the remainder of the Match and may not be replaced by another Team member. Failure to comply with a request to leave the Competition Area violates rule <G27>"""))

rules.append(("G1","""" Drive Team – Each Drive Team shall include up to two Drivers and one Coach. Electronic communications (cell phone, two-way radio, Wi-Fi, Bluetooth, etc.) by Drive Team members after an Alliance has been called from the queue to the Playing Field for its Match are not allowed. The first instance of violating this rule will result in a warning, with any following instances during the tournament resulting in a Minor Penalty. Items that may be mistaken by a casual observer as being in violation should not be brought to the Playing Field. The Driver Station is exempt from this rule, but must be used only for operating the Robot."""))

rules.append(("G2",""" Pre-Match Robot Setup – At the beginning of a Match, each Alliance Robot must be set up on the Playing Field in accordance with section 1.5.1. After Robots have been set up on the Playing Field, Drive Teams are required to stand Completely Inside the Alliance Station at the location (Station one or Station two) specified by the Qualification Match schedule.
	a. During the Qualification Matches, the Blue Alliance Robots are set up on the Playing Field first, unless the Red Alliance waives their right to set up on the Playing Field second.
	b. During the Elimination Matches, the 3rd and 4th seeded Alliance Robots are set up on the Playing Field first, unless the higher seeded Alliance waives their right to set up on the Playing Field second. Alliance color doesn’t change the seeding of a Team during the Elimination Matches. If the 4th seed defeats the 1st seed in the Semi-Finals, they will still have to place their Robot on the field first in the Finals because their seeding will be lower than the 2nd or 3rd seed.
	c. Teams may implicitly waive their right to place their Robots on the Playing Field last by placing their Robots on the Playing Field before or in conjunction with the opposing Alliance. There is no need to notify the referees; Teams waive their right by the act of placing their Robots on the Playing Field.
	d. Teams that unnecessarily delay the beginning of a Match and/or field reset will incur a Minor Penalty for each offense. 
Drive Teams are expected to stage their Robots for a Match, and remove them from the Playing Field afterwards, safely and swiftly. Drive Team efforts that either intentionally or unintentionally delay the start of a Match or the Field reset are not allowed. Examples include, but are not limited to:
- Late arrival to the Playing Field.
- Robot maintenance once on the Playing Field."""))

rules.append(("G3",""" Robot Starting Volume – Before the start of a Match, each Robot in its starting location must not exceed a volume of 18 inches (45.7cm) wide by 18 inches (45.7cm) long by 18 inches (45.7cm) tall. The Alliance identification flag and pre-loaded Scoring Elements may extend Outside the 18-inch (45.7cm) cube volume constraint. An offending Robot will be Disabled and powered off for the Match at the Head Referee’s discretion and must remain on the Playing Field in its starting location for the length of the Match. After the start of a Match, the Robot may extend in any dimension unless restricted by the Game-Specific rules detailed in Section 1.6.3."""))

rules.append(("G4",""" Robot Setup Alignment Devices – Alignment devices are allowed during pre-Match setup if they are constructed from legal components, are part of the Robot, and remain Completely Inside the 18-inch (45.7cm) cube starting volume constraint during the set up process. A Minor Penalty will be assessed to the
Team for violation of this rule. The intent of this rule is to prohibit the use of devices external to the Robot and to prevent the extension of any object or tool Outside the 18-inch (45.7cm) cube starting volume. Humans standing on the other side of the field to aid in aligning the Robot are not allowed."""))

rules.append(("G5",""" Alliance Station – During a Match, the Drivers and Coach must remain Completely Inside their Alliance Station. The first instance of leaving the Alliance Station will result in a warning, with any following instances resulting in a Minor Penalty. Leaving the Alliance Station for safety reasons will not result in a warning or Penalty."""))

rules.append(("G6",""" Starting Game Play Early – Robots that start play of the game (Autonomous or Driver-Controlled Period) prior to competition personnel announcing the start of a Match Period receive a Minor Penalty. Referees have the option of issuing a Major Penalty in place of the Minor Penalty if the early start results in a competitive advantage for the offending Alliance."""))

rules.append(("G7",""" Late Start of the Autonomous Period – Teams participating in the Autonomous Period are expected to press the ”start with 30-second” button on their Driver Station Android device and then place the Driver Station in a hands-off location without delay when field personnel signal the start of the Autonomous Period. A Minor Penalty is assessed for violating this rule. Referees have the option of issuing a Major Penalty in place of the Minor Penalty if the late start results in a competitive advantage for the offending Alliance."""))

rules.append(("G8",""" Stopping Autonomous Period Game Play Early – Drive Teams that use their Driver Station to stop their Robot before the end of the Autonomous Period will receive a Major Penalty. In the case of unsafe Robot behavior, the Drive Team will not be Penalized for stopping the Robot if it is performed with the approval of a referee or Field Technical Advisor."""))

rules.append(("G9",""" Stopping Game Play Late – Robots that do not stop playing the game at the end of the Autonomous or Driver-Controlled Periods when competition personnel or timer software announce the end of a Match period receive a Minor Penalty and the actions of the Robot occurring after the end of a Match period do not count towards their Alliance’s Score. Referees have the option of issuing a Major Penalty in place of the Minor Penalty if the late stop results in a competitive advantage (other than Scoring) for the offending Alliance. Scoring Elements that were launched before the end of the period are eligible to be counted as Scored. Other Robot Scoring achievements that occur after the announced end of the Autonomous Period and before the start of the Driver-Controlled Period do not count towards the Score for the Autonomous or Driver-Controlled Periods. Referees may remove any Scoring Elements from a Scoring Area that are improperly Scored in this manner. The intent of this rule is for Robots to stop playing the game within a reasonable human reaction time following the start of the game sound (i.e., buzzer) signaling the end of the period. Drive Teams should make their best effort to stop game play immediately when the end of period game sound begins. Before the consequences come into play, referees will use their discretion to give Drive Teams an approximate one second grace period following the conclusion of the game sound signaling the end of the period for Robots to stop playing the game."""))

rules.append(("G10",""" Drive Team Contact with the Playing Field or Robot – During a Match, the Drivers and Coaches are prohibited from making contact with the Playing Field, any Game Element, or any Robot. The first instance of contact will result in a warning, with any following instances resulting in a Minor Penalty. Contact that affects Scoring and/or game play will result in issuance of a Yellow Card at the discretion of the referees. Contact with the Playing Field, a Game Element, or a Robot for safety reasons will not result in a
warning or Penalty. For example, a Game Element is launched from a Robot on the Playing Field and it Inadvertently hits a Team member in the Alliance Station and is deflected back onto the field. The Team would NOT receive a Penalty because the Team member was protecting him/herself (safety). However, if that same Game Element is caught and/or directed to a specific location on the Playing Field, the Team may be issued a Penalty."""))

rules.append(("G11",""" Autonomous to Driver-Controlled Period Transition – At the conclusion of the Autonomous Period, Robots will remain in a hands-off state. Field personnel will not enter the field, and will not touch Robots on the field from the Autonomous to Driver Controlled transition."""))

rules.append(("G12",""" Drive Team Coach Driver Station Control – During the Driver-Controlled Period, Robots must be remotely operated only by the Drivers using the Gamepads connected to the Team’s Driver Station and/or by software running in the on-board Robot control system. The first instance of Coach controlling a Robot (for example, operating a Gamepad) will result in a warning, with any following instances resulting in a Major Penalty. During the Driver-Controlled Period, Drive Team Coaches and/or Drivers are allowed to hold the
Important Note: Rule <G11> is a major change for the 2017-2018 season. Volunteers, Coaches and Teams must be prepared for this new transition during the competition season. Team’s Driver Station Android device and interact with it to select an Op Mode, view information displayed on the screen, and initialize, start, stop, and reset the Robot."""))

rules.append(("G13",""" Recording the Score After Objects Come to Rest – Referee scoresheets will be filled out at the end of the Autonomous and Driver-Controlled Periods when all objects on the Playing Field have come to rest. A change in the state of a Game Element or Robot that occurs before a referee records the Score will affect the Match Score. A change in state of a Game Element or Robot after its Score is recorded on the scoresheet will not change an already-recorded Score."""))

rules.append(("G14",""" Robots Deliberately Detaching Parts – Robots may not deliberately detach parts during a Match, or leave mechanisms on the Playing Field. The consequence of deliberately detaching a part is a Minor Penalty if it does not Block an opposing Alliance Robot, Alliance-specific Scoring Element or Scoring Area. If a deliberately-detached component or mechanism affects gameplay by any Robot, the offending Robot will receive a Major Penalty and will be issued a Yellow Card. Robot parts that are released but remain connected by a tether are considered detached for the purposes of this rule. Tethered components that move independent of the main Robot are considered a detached component and are illegal."""))

rules.append(("G15",""" Robots Grasping Game Elements – Robots may not grab, grasp and/or attach to any Game
Element or structure other than Scoring Elements, unless specifically allowed by game-specific rule(s) listed
in Section 1.6.3. The first instance will result in a warning with any following violations resulting in a Major
Penalty."""))

rules.append(("G16",""" Destruction, Damage, Tipping, etc. – Strategies and/or mechanisms aimed solely at the
destruction, damage, tipping over, or entanglement of Robots or Game Elements are not in the spirit of the
FIRST Tech Challenge and are not allowed. However, FIRST Tech Challenge games are highly interactive
and Robot-to-Robot contact and defensive game play should be expected. Some tipping, entanglement, and
damage may occur as a part of normal game play. If the tipping, entanglement, or damage is ruled to be
deliberate or chronic, the offending Team will receive a Major Penalty and a Yellow Card."""))

rules.append(("G17",""" Pinning, Trapping, or Blocking Robots – A Robot cannot cause an opposing Alliance Robot to become Pinned, Trapped, or Blocked for more than five seconds. If a referee determines this rule is violated, the offending Alliance will receive a Minor Penalty for every five seconds that they are in violation. If a referee declares a Pinning, Trapping, or Blocking warning during the Match, the offending Robot must immediately move away at least 3 feet (0.9 m), approximately 1.5 floor tiles, from the Pinned, Trapped, or Blocked Robot. The intent of this Rule is that Drive Teams begin to immediately move their Robots away and have a five second grace period to move the required distance, and NOT that they are permitted to intentionally Block for up to five seconds. A Robot cannot incur this type of Penalty during the Autonomous Period unless it is determined by the Referee to be part of a deliberate strategy and will be penalized as described above. If the violation happens during the Autonomous Period, the first action done by the offending Robot during the Driver Controlled Period must be to move away from the Pinned, Trapped, or Blocked Robot or a Minor Penalty will be assessed immediately and again for every five seconds that they are in violation. Game-specific rule(s) listed in Section 1.6.3 that further define Pinning, Trapping, or Blocking take precedence over this general game rule."""))

rules.append(("G18",""" Forcing an Opponent to Break a Rule – The actions of an Alliance or their Robots shall not cause an opposing Alliance or Robot to break a rule and thus incur Penalties. Any forced rule violations committed by the affected Alliance shall be excused, and no Penalties will be assigned."""))

rules.append(("G19",""" Removing Game Elements from the Playing Field – Robots may not deliberately remove Game Elements from the Playing Field during a Match. Game Elements that Inadvertently fall Outside the Playing Field will be returned to the Playing Field by field personnel at the earliest safe and convenient opportunity at a non-Scoring location approximately where it left the field. Game Elements removed from the Playing Field in an attempt to Score are also not subject to this Penalty. Teams deliberately removing Game Elements from the Playing Field will incur a Minor Penalty per Game Element removed from the Playing Field. Game-specific rule(s) listed in Section 1.6.3 that allow the removal of specified Scoring Elements from the Playing Field take precedence over this general game rule."""))

rules.append(("G20",""" Scoring Elements in Contact with Robots – Scoring Elements in a Scoring Area that are in contact with a Robot on the corresponding Alliance for the Scoring Area have zero Score value when referees record the Score at the end of the Autonomous and Driver-Controlled Periods. Game-specific rule(s) listed in Section 1.6.3 that allow Robot contact with Scoring Elements take precedence over this general game rule."""))

rules.append(("G21",""" Post-Match Removal of Game Elements from Robots – Robots must be designed to permit easy removal of Game Elements from any grasping, containing, or holding mechanism after the Match. Robots should also be able to be removed from the Playing Field without damaging the Playing Field. A Minor Penalty will be assessed for violations of this rule. The intent of this rule is to have timely removal of Robots from the Playing Field following a Match. Drive Teams are expected to stage their Robots for a Match, and remove them from the Playing Field afterwards, safely and swiftly. Drive Team efforts that either intentionally or unintentionally delay the start of a Match or the Field reset are not allowed. Examples include, but are not limited to:
• Failing to exit the Playing Field once instructed by a Referee.
• Failing to remove Driver Stations in a timely manner."""))

rules.append(("G22",""" Robot Manipulation of Scoring Elements – Scoring Elements that are Controlled or Possessed by a Robot are considered to be part of the Robot."""))

rules.append(("G23",""" Robot or Scoring Elements In Two or More Scoring Areas – Robots or Scoring Elements that are In two or more Scoring Areas earn points only for the highest value achievement. If the achievement values are equal, only one achievement counts as Scored. Exceptions to this general rule may be specified in the Game Play section (1.5) or in the game-specific rules."""))

rules.append(("G24",""" Disabled Robot Eligibility - If a referee Disables a Robot, it will not be eligible to Score or earn points for the remainder of the Match. A Disabled Robot (whether referee induced or failure) does not earn penalties after becoming Disabled."""))

rules.append(("G25",""" Playing Field Tolerances – Playing Field and Game Elements will start each Match with tolerances that may vary by as much as +/-1.0 inch (2.5 cm). Teams must design their Robots accordingly."""))

rules.append(("G26",""" Match Replay – Matches are replayed at the discretion of the Head Referee only for a failure of a Game Element or verified Wi-Fi interference that was likely to have impacted which Alliance won the Match. Unexpected Robot behavior in itself will not result in a Match replay. Team-induced failures, such as low battery conditions, processor sleep time-outs, Robot mechanical/electrical/software/communication failures, etc. are NOT valid justifications for a replaying of a Match."""))

rules.append(("G27",""" Egregious Behavior – Egregious Robot or Team member behavior at the Playing Field, as determined by the referees, will result in a Major Penalty and issuance of a Yellow Card and/or Red Card. Subsequent violations will result in Team Disqualification from the tournament. Egregious behavior includes, but is not limited to, repeated and/or flagrant violation of game rules, unsafe behavior or actions, and uncivil behavior towards Drivers, Coaches, competition personnel, or event attendees."""))

rules.append(("G28",""" Inadvertent and Inconsequential - Robot actions that violate a rule may be ruled at the referee’s discretion to be Inconsequential and Inadvertent and will not be Penalized."""))

rules.append(("GS1",""" Drive Teams Touching Robots or Driver Stations after Jewel/Pictograph Randomization – Drive Teams are not allowed to touch or interact with their Robots or Driver Stations once field personnel have begun the randomization process. If this occurs, a Minor Penalty will be assessed per Robot and the affected Robots are not eligible to Score a Jewel/Cryptobox Key in the Autonomous Period. This Penalty only affects the offending Team. The non-offending Alliance Partner Robot remains eligible for the Jewel/Cryptobox Key Scoring achievement."""))

rules.append(("GS2",""" Autonomous Period Robot Keep Out Area – Robots may not go Inside the opposing Alliance’s Area of the Playing Field at any time during the Autonomous Period. A Major Penalty will be assessed for violating this rule and any Scoring that occurs in the opposing Alliance’s Area by the offending Robot will not benefit the offending Alliance. The red and blue gaffer tape on the Playing Field Floor divides the Playing Field into equal sized Alliance Areas. Robots may enter the Glyph Pit at any time. The intent of this rule is to allow Robots to Score their Jewels and Glyphs without defensive play by the opposing Alliance. Inadvertent and Inconsequential incursions will be treated per <G28>"""))

rules.append(("GS3","""" Control/Possession Limits of Glyphs – Once a Match begins, a Robot may Control or Possess a maximum of two (2) Glyphs. Plowing through any quantity of Glyphs is allowed but herding or directing multiple Glyphs to gain a strategic advantage (i.e., Scoring, accessibility, defense) is not allowed. The Penalty for Controlling or Possessing more than two (2) Glyphs is an immediate Minor Penalty for each Glyph above the limit plus an additional Minor Penalty per Glyph for each 5-second interval that this situation continues. A double Major Penalty will be assessed for each Glyph Scored while a Robot Controls or Possesses more than two (2) Glyphs. Continued violation of this rule will escalate to Yellow Cards quickly."""))

rules.append(("GS4",""" Glyph Hoarding – Once an alliance has successfully scored more than 20 Glyphs, the members of the Alliance may not collectively possess/control/block access to more than the number of Glyphs required for the Alliance to completely fill their Cryptoboxes. Violation of this rule will result in an immediate Major Penalty and an additional Minor Penalty assessed for each 5 seconds the rule violation persists per Glyph in excess of the limit. Intentional or repeated violations of this rule will escalate quickly to issuance of Yellow Cards to all members of the Alliance."""))

rules.append(("GS5",""" Control/Possession Limits of Relics – Once a Match begins, a Robot may Control or Possess a maximum of one Relic at a time. The Penalty for Controlling or Possessing more than one Relic is that no Relics will be eligible to be Scored at the end of the Match by either Robot for the Alliance."""))

rules.append(("GS6",""" De-scoring Glyphs – Robots may not remove or re-position Glyphs from their opposing Alliance’s Cryptoboxes. A Double Major Penalty will be assessed for every Glyph illegally removed or re-positioned. Robots are allowed to remove or re-position Glyphs from their own Alliance’s Cryptoboxes. Drive Teams should exercise care when operating around an opposing Alliance’s Cryptobox to mitigate De-scoring."""))

rules.append(("GS7",""" De-scoring Relics – Robots may not remove or re-position Relics In the opposing Alliance’s Recovery Zone. In the event of any re-positioning (for example, if a Blue Relic is dropped into the Blue Recovery Zone, bounces to the Red Recovery Zone and knocks the Red Relic from one Scoring position to another) the opposing Alliance’s Relic is awarded the maximum potential points (40 + 15 = 55). De-scoring an opposing Alliance’s Relic will be penalized, even if it is accidental. This rule supersedes rule <G28>"""))

rules.append(("GS8","""" Interfering with Access to Cryptobox – Robots may not interfere with an opposing Alliance Robot that is In their Alliance’s Safe Zone and attempting to Score a Glyph. A Robot must have a Glyph in its Control to be considered as attempting to Score. The first instance will result in an immediate Major Penalty and an additional Minor Penalty assessed for every five seconds that the rule violation persists. Additional occurrences of violations of this rule will escalate to Yellow Cards quickly."""))

rules.append(("GS9",""" Non-Glyph Game Elements Inside Cryptobox – Glyphs are the only item allowed to be placed In a Cryptobox. A Major Penalty will immediately be assessed for each non-Glyph item (Jewel, Relic, etc.) placed In an opposing Alliance’s Cryptobox. Removal of the illegal Game Element is up to the Alliance that owns the Cryptobox."""))

rules.append(("GS10",""" Controlling or Blocking access to Relics - Robots may not Control, Trap, or Block access to an opposing Alliance’s Relic. The first instance will result in an immediate Major Penalty and an additional Minor Penalty assessed for every five seconds that the rule violation persists. If the referee declares a Controlling, Trapping, or Blocking access Penalty, the offending Robot must move away at least 3 ft. (0.9 m), approximately 1.5 floor tiles from the opponent’s Relic. Additional occurrences of violations of this rule will escalate to Yellow Cards quickly. The intent of this rule is to allow Robot access to their Relics. Blocking means denying ALL access, so general Robot movement with respect to other Robots should not be considered in violation unless there is no other way to traverse the Playing Field to get the Relic. Also, note that this rule requires attempted action on the part of the opposing Alliance."""))

rules.append(("GS11",""" Blocking access to Balancing Stone– During the End Game, Robots may not Block access to the opposing Alliance’s Balancing Stones. The first instance will result in a warning with any following violations resulting in a Major Penalty and an additional Minor Penalty assessed for every five seconds that the rule violation persists. If the referee declares a Blocking access warning during the End Game, the offending Robot must move away at least 3 feet (0.9 m), approximately 1.5 floor tiles from the Blocked Balancing Stone. Failure to move the required 3 feet (0.9 m) within 5 seconds is considered an additional violation and will incur the penalties described above. Additional occurrences of violations of this rule will escalate to Yellow Cards quickly.
The intent of this rule is to allow Robot access to and from their Alliance’s Balancing Stones. Blocking and Trapping means denying ALL access, so general Robot movement with respect to other Robots should not be considered in violation unless there is no other way to traverse the Playing Field to get to the Balancing Stone. Also note that this rule requires attempted access to a Balancing Stone on the part of the opposing Alliance."""))

rules.append(("GS12",""" Balancing Stone Interference – Robots may not interfere with the opposing Alliance’s Robot or Balancing Stone while that Robot is attempting to Balance during the End Game. Once a Robot is in contact with the Balancing Stone this rule will apply. The first instance will result in a warning with any following violations resulting in a Major Penalty and an additional Minor Penalty assessed for every five seconds that the rule violation persists. The intent of this rule is to allow Robots to Balance on the Balancing Stones without interference. Additional occurrences of violations of this rule will escalate to Yellow Cards quickly."""))

rules.append(("GS13",""" Preventing Relic Scoring – Robots may not interfere with opposing Alliance Robots that are attempting to Score a Relic. A Robot must have a Relic in its Possession and be within 24 inches (61 cm), approximately one tile, of the wall facing that Alliance’s Recovery Zones to be considered as attempting to Score. Incidental contact that is Inadvertent and Inconsequential will not be Penalized. The first instance will result in a Major Penalty and an additional Minor Penalty assessed for every five seconds that the rule violation persists."""))

rules.append(("GS14",""" Relic Control - Robots may Control or Possess their own Alliance’s Relics at any time but may only
Score their Relic (i.e. reach over the Playing Field Wall) during the End Game or when the Relic is eligible to
be Scored (whichever is earlier). If a Cryptobox Cipher is correctly solved prior to the start of End Game,
Teams are permitted to Score their Relic early. One (1) Relic may be Scored early for each completed Cipher.
Referees will signal the Alliance when they are allowed to Score a Relic early. Relics that are moved Outside
the Playing Field Wall (by their Alliance) before they are eligible will have zero Score value."""))

rules.append(("GS15",""" Outside Contact during Relic Scoring – Robots may reach over the audience-facing Playing Field Perimeter Wall (and touch the floor outside the Playing Field) only while attempting to Score or attempting to re-position a Relic. Robots may contact the top and outside surface of the Playing Field Perimeter Wall as well as the Recovery Zone mats while attempting to Score a Relic. Robots extending Outside the Playing Field and Relics removed from the Playing Field in an attempt to Score are not subject to rule rules.append(("S2",""" or rules.append(("G19","""". For example, a Robot reaching over the wall while attempting to score a Relic in the Recovery Zone is allowed. Note that rule <S1> still applies, so Robots will need to ensure safe behavior when extended Outside the Playing Field Wall."""))

rules.append(("GS16",""" Scoring Relics - The only legal way to Score a Relic is by placing/dropping it in the Relic Recovery Zone. Relics may not be propelled with any noticeable force (i.e. shooting, launching, flicking, etc.). Illegally launched Relics have zero Score value. Relics that miss the Recovery Zones are not replaced into the Playing Field. They remain where they land and are available for Robots to attempt recovery."""))

commandStr = "~"

def handle_query(query, rules_list, awards_list):
    words = query.lower().split(" ")
    if (words[0].lower() == "award"):
        print("award")
        terms = get_rules_list(awards_list, words[1:])
    elif (words[0].lower() == "rule"):
        print("rule")
        terms = get_rules_list(rules_list, words[1:])
    elif (words[0].lower() == "define"):
        print("definition")
        terms = get_rules_list(definition_list, words[1:])
    else:
        print("nothing")
        return ""
    reply_text = ""
    for term in terms:
        reply_text += term[0] + ":\n" + term[1] + "\n"
    return reply_text

def get_rules_list(rules_list, query_list):
    good_rules = []
    if (len(query_list) == 1):
        for rule in rules_list:
            if(query_list[0].lower() == rule[0].lower()):
                return [rule]
    for rule in rules_list:
        is_good = 0
        is_bad = 0
        for query in query_list:
            if (query not in rule[1].lower()) and (query != rule[0].lower()):
                is_bad += 1
            else:
                is_good += 1
        if (is_good + is_bad) == 0:
            is_bad = 1
        percent = (is_good / (is_good + is_bad))
        if percent >= .75:
            good_rules.append(rule)
    return good_rules

def test_on_message(message):
    global commandStr
    if message[0:len(commandStr)] == commandStr:
        print("IN")
        test_handle_message(message[len(commandStr):])
def test_handle_message(messageBody):
    global commandStr
    print(messageBody)
    if (messageBody == "help" or messageBody == "about"):
        print(getHelpText("PLACEHOLDER"))
    else:
        reply = handle_query(messageBody, rules, awards)
        print(reply)
        if not reply == "":
            print(reply)


def getHelpText(sender):
    reply = "@" + str(sender) + " this bot is pretty simple:"
    reply += "\n"
    reply += commandStr + "rule QUERY_HERE -- will search the rules, returning rules containing 75% or more of the words in QUERY"
    reply += "\n"
    reply += commandStr + "rule RULE_NAME -- will also return the rule with the name RULE_NAME"
    reply += "\n"
    reply += commandStr + "award AWARD -- will tell you the description of AWARD in Game Manual Part 1"
    return reply


print("Setting up Client")
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    global commandStr
    if message.content[0:len(commandStr)] == commandStr:
        messageCommand = message.content[len(commandStr):]
        print("Parsing: " + message.content)
        if(messageCommand == "about" or messageCommand == "help"):
            reply = getHelpText(str(message.author)[-5:])
        else:
            print("handling query")
            reply = handle_query(messageCommand, rules, awards)
        print("Reply is:" + str(reply) + "")
        if reply == "":
            await client.send_message(message.channel, "Sorry, I couldn't find anything about that query")
        else:
            print(reply)
            while(len(reply) > 2000):
                await client.send_message(message.channel, reply[0:2000])
                reply = reply[2000:]
            await client.send_message(message.channel, reply)

useBot = True
if (useBot):
    print("Running Bot")
    client.run(login_token)
    # https://discordapp.com/api/oauth2/authorize?client_id=400342210345828352&permissions=3072&scope=bot
else:
    while True:
        query = input("What query")
        test_on_message(query)