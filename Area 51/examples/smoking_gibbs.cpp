#include <pracmln/mln.h>

int main(int argc, char **argv)
{
  // create a mln object
  MLN mln;

  // initialize the object (loading python packages, etc.)
  if(!mln.initialize()){
    // error
  }

  std::vector<std::string> query;
  query.push_back("some query");

  // change settings, give input files, etc.
  mln.setQuery(query);
  mln.setMLN("./data/smokers/mlns/smoking_trained.mln");
  mln.setDB("./data/smokers/dbs/smoking-test.db");
  //mln.setMethod("GibbsSampling");

  std::vector<std::string> results;
  std::vector<double> probabilities;

  // execute inference
  if(mln.infer(results, probabilities)){
    // error
  }

  // do something with the results

  return 0;
}
