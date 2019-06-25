package Bell.pokebattle;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.util.Log;
import android.util.Pair;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;
import java.util.Vector;

import static java.lang.Double.parseDouble;
import static java.lang.Integer.parseInt;


class Types {

   private static HashMap<String, Type> stringToTypes = new HashMap<>();
   private static HashMap<Integer, Type> intToTypes = new HashMap<>();

   static {
      stringToTypes.put("normal",Type.normal);
      stringToTypes.put("fighting",Type.fighting);
      stringToTypes.put("flying",Type.flying);
      stringToTypes.put("poison",Type.poison);
      stringToTypes.put("ground",Type.ground);
      stringToTypes.put("rock",Type.rock);
      stringToTypes.put("bug",Type.bug);
      stringToTypes.put("ghost",Type.ghost);
      stringToTypes.put("steel",Type.steel);
      stringToTypes.put("fire",Type.fire);
      stringToTypes.put("water",Type.water);
      stringToTypes.put("grass",Type.grass);
      stringToTypes.put("electric",Type.electric);
      stringToTypes.put("psychic",Type.psychic);
      stringToTypes.put("ice",Type.ice);
      stringToTypes.put("dragon",Type.dragon);
      stringToTypes.put("dark",Type.dark);
      stringToTypes.put("fairy",Type.fairy);
      intToTypes.put(1,Type.normal);
      intToTypes.put(2,Type.fighting);
      intToTypes.put(3,Type.flying);
      intToTypes.put(4,Type.poison);
      intToTypes.put(5,Type.ground);
      intToTypes.put(6,Type.rock);
      intToTypes.put(7,Type.bug);
      intToTypes.put(8,Type.ghost);
      intToTypes.put(9,Type.steel);
      intToTypes.put(10,Type.fire);
      intToTypes.put(11,Type.water);
      intToTypes.put(12,Type.grass);
      intToTypes.put(13,Type.electric);
      intToTypes.put(14,Type.psychic);
      intToTypes.put(15,Type.ice);
      intToTypes.put(16,Type.dragon);
      intToTypes.put(17,Type.dark);
      intToTypes.put(18,Type.fairy);
   }

   public static boolean addEfficacy(int att, int def, double eff) {
      return intToTypes.get(att).addEffective(intToTypes.get(def), eff);
   }

   public static Type stringToType(String str) {
      if(stringToTypes.containsKey(str))
         return stringToTypes.get(str);
      return Type.bad;
   }

   public static Type intToType(int id) {
      if(intToTypes.containsKey(id))
         return intToTypes.get(id);
      return Type.bad;
   }

   public enum Type {
      normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass,
      electric, psychic, ice, dragon, dark, fairy, bad;

      HashMap<Type, Double> effective = new HashMap<>();
      boolean addEffective(Type newType, double effectiveValue) {
         if(effective.containsKey(newType))
            return false;
         effective.put(newType, effectiveValue);
         return true;
      }
      double getEffective(Type opp) {
         if(effective.containsKey(opp))
            return effective.get(opp);
         return 0;
      }
   };

}

public class MainActivity extends AppCompatActivity {

   private TextView textView;
   //private ScrollView display;
   private LinearLayout linearScroll;
   //public Types typeSystem = new Types();
   private TreeMap<Integer, Pokemon> pokedex = new TreeMap<>();
   private TreeMap<Integer, Move> movedex = new TreeMap<>();

   private UserPokemon poke1, poke2;

   private Resources res;

   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);

      textView = findViewById(R.id.info);
      linearScroll = findViewById(R.id.linearScroll);

      res = getResources();

      textView.setText("Started");
      loadTypeEfficacy();
      loadPokedex();
      loadPokemonStats();
      loadMovedex();

      //Start user Selection of pokemon
      //textView.setText("Please Select a Pokemon");
      showPokemonSelect();

   }

   private void loadTypeEfficacy() {
      //Read Type Efficacy text file
      try {
         InputStream in_s = res.openRawResource(R.raw.type_efficacy);
         BufferedReader reader = new BufferedReader(new InputStreamReader(in_s));

         //Throw away the first line
         String line = reader.readLine();
         //get all of the lines from the file
         while ((line = reader.readLine()) != null) {
            String[] lineStrings = line.split(",");
            int att = parseInt(lineStrings[0]);
            int def = parseInt(lineStrings[1]);
            double eff = parseDouble(lineStrings[2]) / 100;
            Types.addEfficacy(att, def, eff);
         }
      } catch (Exception e) {
         // e.printStackTrace();
         textView.setText("Error: Something went Wrong when reading Type Efficacy");
      }
   }

   private void loadPokedex() {
      String packageName = getPackageName();
      //Read pokemon text file
      try {
         InputStream in_s = res.openRawResource(R.raw.pokemon);
         BufferedReader reader = new BufferedReader(new InputStreamReader(in_s));

         //Throw away the first line
         String line = reader.readLine();
         //get all of the lines from the file
         while ((line = reader.readLine()) != null) {
            String[] lineStrings = line.split(",");
            int id = parseInt(lineStrings[0]);
            if (id >= 721) break;
            String imgName = "poke" + id;
            //Log.d("pokeImg", imgName);
            //get image
            int iconInt = getResources().getIdentifier(imgName, "drawable", packageName);
            //int iconInt = R.drawable.poke1;
            //Log.d("pokeImg", imgName + ": " + iconInt);

            //create new pokemon
            Pokemon temp = new Pokemon(id, lineStrings[1], iconInt);
            //add to pokedex
            pokedex.put(id, temp);
         }
      } catch (Exception e) {
         // e.printStackTrace();
         textView.setText("Error: Something went Wrong when reading pokemon");
      }
   }

   private void loadPokemonStats() {
      //Read pokemon stats text file
      try {
         InputStream in_s = res.openRawResource(R.raw.pokemon_stats);
         BufferedReader reader = new BufferedReader(new InputStreamReader(in_s));

         //Throw away the first line
         String line = reader.readLine();
         //get all of the lines from the file
         while ((line = reader.readLine()) != null) {
            String[] lineStrings = line.split(",");
            int id = parseInt(lineStrings[0]);
            int statID = parseInt(lineStrings[1]);
            int statVal = parseInt(lineStrings[2]);
            if (pokedex.containsKey(id))
               pokedex.get(id).addStat(statID, statVal);
            else break;
         }
      } catch (Exception e) {
         // e.printStackTrace();
         textView.setText("Error: Something went Wrong when reading pokemon stats");
      }

      //Read pokemon types file
      try {
         InputStream in_s = res.openRawResource(R.raw.pokemon_types);
         BufferedReader reader = new BufferedReader(new InputStreamReader(in_s));

         //Throw away the first line
         String line = reader.readLine();
         //get all of the lines from the file
         while ((line = reader.readLine()) != null) {
            //Log.d("pokemonTypes", line);
            String[] lineStrings = line.split(",");
            int id = parseInt(lineStrings[0]);
            int typeID = parseInt(lineStrings[1]);
            int typeSlot = parseInt(lineStrings[2]);
            if (pokedex.containsKey(id))
               pokedex.get(id).addType(typeID, typeSlot);
            else break;
         }
      } catch (Exception e) {
         // e.printStackTrace();
         textView.setText("Error: Something went Wrong when pokemon Types");
      }
   }

   private void loadMovedex() {
      //Read moves text file
      try {
         InputStream in_s = res.openRawResource(R.raw.moves);
         BufferedReader reader = new BufferedReader(new InputStreamReader(in_s));

         //Throw away the first line
         String line = reader.readLine();
         //get all of the lines from the file
         while ((line = reader.readLine()) != null) {
            String[] lineStrings = line.split(",");
            int id = 0, power = 0, typeID = 0, pp = 0, accuracy = 0;
            String name = "";
            boolean priority = false;
            if (lineStrings[0] != "") id = parseInt(lineStrings[0]);
            if (lineStrings[1] != "") name = lineStrings[1];
            if (lineStrings[3] != "") typeID = parseInt(lineStrings[3]);
            if (lineStrings[4] != "") power = parseInt(lineStrings[4]);
            if (lineStrings[5] != "") pp = parseInt(lineStrings[5]);
            if (lineStrings[6] != "") accuracy = parseInt(lineStrings[6]);
            if (lineStrings[7] != "") priority = (parseInt(lineStrings[7]) == 1);

            //skip status/non damaging moves or anything else that stayed 0
            if (power == 0 || typeID == 0 || id == 0 || pp == 0) continue;
            Move temp = new Move(id, power, pp, accuracy, priority, name, typeID);
            //Log.d("Move", "" + temp);
            movedex.put(id, temp);
         }
      } catch (Exception e) {
         // e.printStackTrace();
         textView.setText("Error: Something went Wrong when reading Moves");
         Log.d("moveRead", "Move failed to load");
      }
   }

   private void showPokemonSelect() {
      linearScroll.removeAllViews();
      textView.setText("Select a Pokemon.");
      //TODO add search functionality (by name or number)

      for(final Map.Entry<Integer, Pokemon> poke: pokedex.entrySet()) {
         Button button = poke.getValue().toLayout(this);
         button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               textView.setText("Selected: " + poke.getValue());
               showMoveSelect(poke.getValue());
            }
         });
         linearScroll.addView(button);
      }
   }

   private void showMoveSelect(final Pokemon selectedPoke) {
      linearScroll.removeAllViews();
      textView.setText("Select up to 4 moves for " + selectedPoke.getName());
      final Vector<Move> moves = new Vector<>();
      final int MAX_MOVES = 4;
      //TODO add search functionality (and filter by type?)

      for(final Map.Entry<Integer, Move> move: movedex.entrySet()) {
         Button button = move.getValue().toLayout(this);
         button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               String movesText = "";
               moves.add(move.getValue());
               for(Move move : moves) {
                  movesText += move + "\n";
               }
               textView.setText(movesText);
               if(moves.size() == MAX_MOVES) {
                  linearScroll.removeAllViews();
                  UserPokemon temp = new UserPokemon(selectedPoke, moves);
                  if(poke1 == null) {
                     poke1 = temp;
                     showPokemonSelect();
                  }
                  else {
                     poke2 = temp;
                     //start Battle!!!!
                     battle(1);
                  }
               }
            }
         });
         linearScroll.addView(button);
      }
   }

   private void battle(final int playerTurn) {
      Log.d("endGame", "Poke1 hp: " + poke1.getCurrentHp());
      Log.d("endGame", "Poke2 hp: " + poke2.getCurrentHp());
      if(poke1.getCurrentHp() <= 0) {
         endGame(poke2, poke1);
         return;
      }
      if(poke2.getCurrentHp() <= 0) {
         endGame(poke1, poke2);
         return;
      }
      //oh boy
      Log.d("Battle", "Loading Pokemon Views");
      linearScroll.removeAllViews();
      textView.setText("Player " + playerTurn + " select a Move.");
      Vector<Pair<Integer, Button>> moveButtons;
      if(playerTurn == 1) {
         linearScroll.addView(poke2.toLayout(false, this));
         linearScroll.addView(poke1.toLayout(true, this));
         moveButtons = poke1.getMoveButtons(this);
      } else {
         linearScroll.addView(poke1.toLayout(false, this));
         linearScroll.addView(poke2.toLayout(true, this));
         moveButtons = poke2.getMoveButtons(this);
      }
      for(final Pair<Integer, Button> moveButton: moveButtons) {
         linearScroll.addView(moveButton.second);
         moveButton.second.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               if(playerTurn == 1) {
                  poke1.useMove(moveButton.first, poke2);
                  Log.d("useMove", "opp hp outside: " + poke2.getCurrentHp());
                  battle(2);
               } else {
                  poke2.useMove(moveButton.first, poke1);
                  Log.d("useMove", "opp hp outside: " + poke1.getCurrentHp());
                  battle(1);
               }
            }
         });
      }
      Log.d("Battle", "Select Move");
   }

   public void endGame(UserPokemon winningPoke, UserPokemon losingPoke) {
      linearScroll.removeAllViews();
      String winText = "Congrats!\n";
      winText += winningPoke.getName() + " has defeated " + losingPoke.getName() + "\n";
      textView.setText(winText);
   }

}


class Pokemon {
   private final static int hpID = 1, attackID = 2, defenceID = 3;
   private final static int specAttackID = 4, specDefenceID = 5, speedID = 6;

   private int ID = 0;
   private int hp = 0;
   private int attack = 0;
   private int specAttack = 0;
   private int defence = 0;
   private int specDefence = 0;
   private int speed = 0;
   private String name;
   private int iconID;
   private Types.Type type1;
   private Types.Type type2;
   public Pokemon() {
      name = "Missing No";
   }
   //crappy constructor needs refactoring later with some sort of data validation
   public Pokemon (int newId, String newName, int newIcon) {
      ID = newId;
      iconID = newIcon;
      name = newName;
   }
   public Pokemon(Pokemon poke)
   {
      ID = poke.getID();
      name = poke.getName();
      iconID = poke.getIconID();
      hp = poke.getHp();
      attack = poke.getAttack();
      specAttack = poke.getSpecAttack();
      defence = poke.getDefence();
      specDefence = poke.getSpecDefence();
      speed = poke.getSpeed();
      type1 = poke.getType1();
      type2 = poke.getType2();
   }
   public Pokemon(int newID, String newName, int newHP, int newAttack, int newSpecAttack, int newDefence,
                  int newSpecDefence, int newSpeed, Types.Type newType1, Types.Type newType2)
   {
      ID = newID;
      name = newName;
      hp = newHP;
      attack = newAttack;
      specAttack = newSpecAttack;
      defence = newDefence;
      specDefence = newSpecDefence;
      speed = newSpeed;
      type1 = newType1;
      type2 = newType2;
   }

   public boolean addStat(int statID, int statVal) {
      if(statID == hpID) {
         hp = statVal;
         return true;
      } else if (statID == attackID) {
         attack = statVal;
         return true;
      } else if (statID == defenceID) {
         defence = statVal;
         return true;
      } else if (statID == specAttackID) {
         specAttack = statVal;
         return true;
      } else if (statID == specDefenceID) {
         specDefence = statVal;
         return true;
      } else if (statID == speedID) {
         speed = statVal;
         return true;
      }
      return false;
   }

   public boolean addType(int typeID, int typeSlot) {
      if(typeSlot == 1) {
         type1 = Types.intToType(typeID);
         return true;
      } else if (typeSlot == 2) {
         type2 = Types.intToType(typeID);
         return true;
      }
      return false;

   }

   public String toString() {
      String typeString = " Type:";
      if(type1 != null) typeString += " " + type1;
      if(type2 != null) typeString += " " + type2;
      return ID + ": " + name + ": Hp:" + hp + typeString;
   }

   public Button toLayout(Context context) {
      Pokemon thisPoke = this;
      Button button = new Button(context);
      button.setText(toString());
      button.setCompoundDrawablesWithIntrinsicBounds(iconID, 0,iconID,0);
      return button;
   }
   public int getID() {
      return ID;
   }
   public void setID(int ID) {
      this.ID = ID;
   }
   public void setHp(int hp) {
      this.hp = hp;
   }
   public int getAttack() {
      return attack;
   }
   public void setAttack(int attack) {
      this.attack = attack;
   }
   public int getSpecAttack() {
      return specAttack;
   }
   public void setSpecAttack(int specAttack) {
      this.specAttack = specAttack;
   }
   public int getDefence() {
      return defence;
   }
   public void setDefence(int defence) {
      this.defence = defence;
   }
   public int getSpecDefence() {
      return specDefence;
   }
   public void setSpecDefence(int specDefence) {
      this.specDefence = specDefence;
   }
   public int getSpeed() {
      return speed;
   }
   public void setSpeed(int speed) {
      this.speed = speed;
   }
   public void setName(String name) {
      this.name = name;
   }
   public int getIconID() {
      return iconID;
   }
   public void setIconID(int iconID) {
      this.iconID = iconID;
   }
   public Types.Type getType1() {
      return type1;
   }
   public void setType1(Types.Type type1) {
      this.type1 = type1;
   }
   public Types.Type getType2() {
      return type2;
   }
   public void setType2(Types.Type type2) {
      this.type2 = type2;
   }
   public String getName() {
      return name;
   }
   public int getHp() {
      return hp;
   }
}

class Move {
   private int id = 0, power = 0, pp = 0, accuracy = 0;
   private boolean priority = false;
   private String name;
   private Types.Type type;

   public Move(int id, int power, int pp, int accuracy, boolean priority, String name, int typeID) {
      this.id = id;
      this.power = power;
      this.pp = pp;
      this.accuracy = accuracy;
      this.priority = priority;
      this.name = name;
      this.type = Types.intToType(typeID);
   }

   public Move() {
      name = "bad";
   }

   public Types.Type getType() {
      return type;
   }

   public int getPP() {
      return pp;
   }

   public int use() {
      if(pp-- != 0) {
         return power;
      } else {
         return 0;
      }
   }

   public String toString() {
      return name + " type: " + type + " power: " + power + " pp: " + pp + " accuracy: " + accuracy;
   }

   public Button toLayout(Context context) {
      Button button = new Button(context);
      button.setText(toString());
      return button;
   }


}

class UserPokemon extends Pokemon {
   public static final int MAX_MOVES = 4;
   private int currentHp;
   private Vector<Move> moves;

   public UserPokemon(Pokemon poke, Vector<Move> newMoves) {
      super(poke);
      currentHp = poke.getHp();
      //if too many moves only take first 4
      if(newMoves.size() > MAX_MOVES) {
         for(int i = 0; i < MAX_MOVES; i++) {
            moves.add(newMoves.get(i));
         }
      }
      else
         moves = newMoves;
   }

   public int getCurrentHp() {
      return currentHp;
   }

   public double getHpPercent() {
      return (double)currentHp / getHp();
   }

   public String toString() {
      String returnStr = super.toString() + "\n";
      for(Move move : moves)
         returnStr += move + "\n";

      return returnStr;
   }

   public void takeDamage(int damage) {
      currentHp -= damage;
   }

   public void useMove(int moveIndex, UserPokemon opp) {
      Move move = moves.get(moveIndex);
      float stab = 1;
      //check for same type attack bonus
      if(move.getType() == getType1() || move.getType() == getType2()) {
         stab = 1.5f;
      }
      float efective = 1;
      //check if move is effective
      efective *= move.getType().getEffective(opp.getType1());
      efective *= move.getType().getEffective(opp.getType2());
      //calculate damage
      int damage = Math.round(move.use() * getAttack() * efective * stab / opp.getDefence());
      Log.d("useMove", "damage: " + damage);
      //deal damage
      opp.takeDamage(damage);
      Log.d("useMove", "opp hp: " + opp.getCurrentHp());;
   }

   public LinearLayout toLayout(boolean isPlayer, Context context) {
      LinearLayout layout = new LinearLayout(context);

      ImageView pokemonImage = new ImageView(context);
      Drawable draw = context.getResources().getDrawable(getIconID(), null);
      pokemonImage.setImageDrawable(draw);
      //pokemonImage.setImageResource(getIconID());

      String pokeText = getName() + " " + getType1() + " " + getType2() + " HP: " + currentHp + "\n";
      TextView pokemonText = new TextView(context);
      pokemonText.setText(pokeText);
      pokemonText.setTextSize(18);
      pokemonText.setTextColor(context.getResources().getColor(R.color.colorPrimaryDark, null));

      //set up right and left layouts
      LinearLayout.LayoutParams image = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.MATCH_PARENT);
      image.weight = 1.0f;
      image.width = 200;
      image.height = 200;
      LinearLayout.LayoutParams text = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.MATCH_PARENT);
      text.weight = 1.0f;


      if(isPlayer) {
         //put pokemon image on right
         image.gravity = Gravity.RIGHT;
         pokemonImage.setLayoutParams(image);
         //put text on left
         text.gravity = Gravity.LEFT;
         pokemonText.setLayoutParams(text);
         layout.addView(pokemonImage);
         layout.addView(pokemonText);
      } else {
         //put text on left
         text.gravity = Gravity.LEFT;
         pokemonText.setLayoutParams(text);
         //put image on right
         image.gravity = Gravity.RIGHT;
         pokemonImage.setLayoutParams(image);
         layout.addView(pokemonText);
         layout.addView(pokemonImage);
      }

      return layout;
   }

   public Vector<Pair<Integer, Button>> getMoveButtons(Context context) {
      Vector<Pair<Integer, Button>> buttons = new Vector<>();
      for(int i = 0; i < moves.size(); i++) {
         if(moves.get(i).getPP() != 0)
            buttons.add(Pair.create(i, moves.get(i).toLayout(context)));
      }
      if(buttons.size() == 0) {
         //add move struggle
      }
      return buttons;
   }

}