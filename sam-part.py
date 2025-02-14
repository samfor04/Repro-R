s_sample <- function(u, theta) {
  # Extract the mean (location) and std. dev (scale) from theta
  mean <- theta[1]
  sd <- theta[2]
   
  # Determine the number of samples and dimensions from the seed matrix u
  # are determined from the `u` matrix.
  num_samples <- nrow(u)
  num_dimensions <- ncol(u)
   
  # Initialize a matrix to store the samples
  samples <- matrix(0, nrow = num_samples, ncol = num_dimensions)
   
  # Generate samples from a location-scale normal distribution for each dimension 
  # loop iterates over each dimension, generating set of random nums. from a normal distribution 
  # w/  specified mean and std. dev.for that dimension. 
  # These nums are then added to the `samples` matrix.
  for (i in  1:num_dimensions) {
    samples[, i] <- rnorm(num_samples, mean = mean[i], sd = sd[i])
  }
   
  return(samples) # matrix of simulated samples returned
}

# optimize for loop,, num_samples * num_dimensions,, 
# apply diff privacy method to s_sample,, clamp data (lower/upper),, use p_max, P-min
## clamp data,, add noise
# take mean/sample variance -> R x 2 matrix


# location-scale normal distribution -> the T statistic could be computed as the sum of sqrd diffs between each simulated value and 
# the observed data, -> summed across all dimensions.

T_calc <- function(S, theta) {
  # Extract the mean (location) and standard deviation (scale) from theta
  mean <- theta[1]
  sd <- theta[2]
   
  # Calculate the T statistic for each row in S
  # Here we assume a simple T statistic based on the difference from the mean
  T_values <- apply(S,  1, function(x) {
    diff <- x - mean
    sum(diff * diff)
  })
   
  return(T_values)
}

# assume mahalanobis
