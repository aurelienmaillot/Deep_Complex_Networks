import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras import constraints
from tensorflow.keras import regularizers
from tensorflow.keras import initializers
from tensorflow.keras.layers import InputSpec



'COMPLEX DENSE'
class complex_Dense(tf.keras.layers.Layer):
    """
    tf.keras.layers.Dense(
        units, activation=None, use_bias=True, kernel_initializer='glorot_uniform',
        bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None,
        activity_regularizer=None, kernel_constraint=None, bias_constraint=None,
        **kwargs
    )
    """
    def __init__ (self, units = 512,
                        activation = None,
                        use_bias   = True, 
                        kernel_initializer = 'glorot_uniform',
                        bias_initializer   = 'zeros', 
                        kernel_regularizer = None, 
                        bias_regularizer   = None,
                        activity_regularizer = None, 
                        kernel_constraint    = None, 
                        bias_constraint      = None):
        
        super(complex_Dense, self).__init__()

        self.units = units
        self.activation = activation
        self.use_bias   = use_bias
        self.kernel_initializer = kernel_initializer
        self.bias_initializer   = bias_initializer
        self.kernel_regularizer = kernel_regularizer
        self.bias_regularizer   = bias_regularizer
        self.activity_regularizer = activity_regularizer
        self.kernel_constraint    = kernel_constraint
        self.bias_constraint      = bias_constraint
        
        
    def build (self, inputs_shape):
        
        self.real_Dense = tf.keras.layers.Dense(units = self.units, 
                                                activation = self.activation, 
                                                use_bias   = self.use_bias, 
                                                kernel_initializer = self.kernel_initializer,
                                                bias_initializer   = self.bias_initializer, 
                                                kernel_regularizer = self.kernel_regularizer,
                                                bias_regularizer   = self.bias_regularizer,
                                                activity_regularizer = self.activity_regularizer, 
                                                kernel_constraint    = self.kernel_constraint,
                                                bias_constraint      = self.bias_constraint)
        
        self.imag_Dense = tf.keras.layers.Dense(units = self.units, 
                                                activation = self.activation, 
                                                use_bias   = self.use_bias, 
                                                kernel_initializer = self.kernel_initializer,
                                                bias_initializer   = self.bias_initializer, 
                                                kernel_regularizer = self.kernel_regularizer,
                                                bias_regularizer   = self.bias_regularizer,
                                                activity_regularizer = self.activity_regularizer, 
                                                kernel_constraint    = self.kernel_constraint,
                                                bias_constraint      = self.bias_constraint)
        
        super(complex_Dense, self).build(inputs_shape)
        

    def call (self, real_inputs, imag_inputs):

        real_outputs = self.real_Dense(real_inputs) - self.imag_Dense(imag_inputs)
        imag_outputs = self.imag_Dense(real_inputs) + self.real_Dense(imag_inputs)

        return real_outputs, imag_outputs



'COMPLEX CONVOLUTION 2D'
class complex_Conv2D (tf.keras.layers.Layer):
    

    def __init__(self, 
                filters = 32,
                kernel_size = (3, 3), 
                strides = (2, 2), 
                padding = "same",
                activation = None,
                use_bias   = True,
                kernel_initializer = 'glorot_uniform',
                bias_initializer   = 'zeros'):
        
        super(complex_Conv2D, self).__init__()
        
        self.filters = filters
        self.kernel_size = kernel_size
        self.strides     = strides
        self.padding     = padding
        self.activation  = activation
        self.use_bias    = use_bias
        self.kernel_initializer = kernel_initializer
        self.bias_initializer   = bias_initializer
        
        
    def build (self, inputs_shape):
        
        self.real_Conv2D = tf.keras.layers.Conv2D(filters = self.filters,
                                                kernel_size = self.kernel_size, 
                                                strides = self.strides,
                                                padding = self.padding,
                                                activation = self.activation,
                                                use_bias = self.use_bias,
                                                kernel_initializer = self.kernel_initializer,
                                                bias_initializer = self.bias_initializer) 

        self.imag_Conv2D = tf.keras.layers.Conv2D(filters = self.filters,
                                                kernel_size = self.kernel_size, 
                                                strides = self.strides,
                                                padding = self.padding,
                                                activation = self.activation,
                                                use_bias = self.use_bias,
                                                kernel_initializer = self.kernel_initializer,
                                                bias_initializer = self.bias_initializer) 
        
        super(complex_Conv2D, self).build(inputs_shape)

        
    def call(self, real_inputs, imag_inputs):
        
        real_outputs = self.real_Conv2D(real_inputs) - self.imag_Conv2D(imag_inputs)
        imag_outputs = self.imag_Conv2D(real_inputs) + self.real_Conv2D(imag_inputs)
        
        return real_outputs, imag_outputs



'COMPLEX CONV 2D TRANSPOSE'
class complex_Conv2DTranspose (tf.keras.layers.Layer):


    def __init__(self,  filters = 32,
                        kernel_size = (3, 3), 
                        strides = (2, 2), 
                        padding = "same",
                        activation = None,
                        use_bias   = True,
                        kernel_initializer = 'glorot_uniform',
                        bias_initializer   = 'zeros'):
        
        super(complex_Conv2DTranspose, self).__init__()

        self.filters = filters
        self.kernel_size = kernel_size
        self.strides     = strides
        self.padding     = padding
        self.activation  = activation
        self.use_bias    = use_bias
        self.kernel_initializer = kernel_initializer
        self.bias_initializer   = bias_initializer
        
        
    def build (self, inputs_shape):

        self.real_Conv2DTranspose = tf.keras.layers.Conv2DTranspose(filters = self.filters,
                                                        kernel_size = self.kernel_size, 
                                                        strides = self.strides, 
                                                        padding = self.padding, 
                                                        activation = self.activation, 
                                                        use_bias = self.use_bias,
                                                        kernel_initializer = self.kernel_initializer, 
                                                        bias_initializer = self.bias_initializer)

        self.imag_Conv2DTranspose = tf.keras.layers.Conv2DTranspose(filters = self.filters,
                                                        kernel_size = self.kernel_size, 
                                                        strides = self.strides, 
                                                        padding = self.padding, 
                                                        activation = self.activation, 
                                                        use_bias = self.use_bias,
                                                        kernel_initializer = self.kernel_initializer, 
                                                        bias_initializer = self.bias_initializer)
        
        super(complex_Conv2DTranspose, self).build(inputs_shape)

        
    def call (self, real_inputs, imag_inputs):

        real_outputs = self.real_Conv2DTranspose(real_inputs) - self.imag_Conv2DTranspose(imag_inputs)
        imag_outputs = self.imag_Conv2DTranspose(real_inputs) + self.real_Conv2DTranspose(imag_inputs)

        return real_outputs, imag_outputs



'COMPLEX POOLING'
class complex_MaxPooling (tf.keras.layers.Layer):

    def __init__(self, pool_size = (2, 2), strides = (1, 1), padding = "same"):

        super(complex_MaxPooling, self).__init__()

        self.pool_size = pool_size
        self.strides   = strides
        self.padding   = padding


    def build (self, inputs_shape):
        
        self.real_maxpooling = tf.keras.layers.MaxPool2D(pool_size = self.pool_size, 
                                                        strides = self.strides, 
                                                        padding = self.padding)
        
        self.imag_maxpooling = tf.keras.layers.MaxPool2D(pool_size = self.pool_size, 
                                                        strides = self.strides, 
                                                        padding = self.padding)
        
        super(complex_MaxPooling, self).build(inputs_shape)
        

    def call (self, real_inputs, imag_inputs):

        real_outputs = self.real_maxpooling(real_inputs)
        imag_outputs = self.imag_maxpooling(imag_inputs)

        return real_outputs, imag_outputs



'NAIVE BATCH NORMALIZATION'
class complex_NaiveBatchNormalization (tf.keras.layers.Layer):
    '''
    tf.keras.layers.BatchNormalization(
        axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,
        beta_initializer='zeros', gamma_initializer='ones',
        moving_mean_initializer='zeros', moving_variance_initializer='ones',
        beta_regularizer=None, gamma_regularizer=None, beta_constraint=None,
        gamma_constraint=None, renorm=False, renorm_clipping=None, renorm_momentum=0.99,
        fused=None, trainable=True, virtual_batch_size=None, adjustment=None, name=None,
        **kwargs

        selfaxis = -1, 
        momentum = 0.99, 
        epsilon = 0.001, 
        center = True, 
        scale = True,
        beta_initializer = 'zeros', 
        gamma_initializer = 'ones',
        moving_mean_initializer = 'zeros',
        moving_variance_initializer = 'ones',
        beta_regularizer = None, 
        gamma_regularizer = None, 
        beta_constraint = None,
        gamma_constraint = None,
        renorm = False,
        renorm_clipping = None, 
        renorm_momentum = 0.99,
        fused = None, 
        trainable = True, 
        virtual_batch_size = None,
        adjustment = None

        self.momoentum = momentum
        self.epsilon   = epsilon
        self.center    = center
        self.scale     = scale 
        self.beta_initializer            = beta_initializer
        self.gamma_initializer           = gamma_initializer
        self.moving_mean_initializer     = moving_mean_initializer
        self.moving_variance_initializer = moving_variance_initializer
        self.beta_regularizer            = beta_regularizer
        self.gamma_regularizer           = gamma_regularizer
        self.beta_constraint             = beta_constraint
        self.gamma_constraint            = gamma_constraint
        self.renorm                      = renorm
        self.renorm_clipping             = renorm_clipping
        self.renorm_momentum             = renorm_momentum
        self.fused                       = fused
        self.trainable                   = trainable
        self.virtual_batch_size          = virtual_batch_size
        self.adjustment                  = adjustment

        momentum = self.momentum,
        epsilon = self.epsilon,
        center = self.center,
        scale = self.scale,
        beta_initializer = self.beta_initializer,
        gamma_initializer = self.gamma_initializer,
        moving_mean_initializer = self.moving_mean_initializer,
        moving_variance_initializer = self.moving_variance_initializer,
        beta_regularizer = self.beta_regularizer,
        gamma_regularizer = self.gamma_regularizer,
        beta_constraint = self.beta_constraint,
        gamma_constraint = self.gamma_constraint,
        renorm = self.renorm,
        renorm_clipping = self.renorm_clipping,
        renorm_momentum = self.renorm_momentum,
        fused = self.fused,
        trainable = self.trainable,
        virtual_batch_size = self.virtual_batch_size,
        adjustment = self.adjustment
    )
    '''
    def __init__ (self):

        super(complex_NaiveBatchNormalization, self).__init__()

        self.real_batchnormalization = tf.keras.layers.BatchNormalization()

        self.imag_batchnormalization = tf.keras.layers.BatchNormalization()
        

    def call (self, real_inputs, imag_inputs, training = True):

        real_outputs = self.real_batchnormalization (real_inputs, training = training)
        imag_outputs = self.imag_batchnormalization (imag_inputs, training = training)

        return real_outputs, imag_outputs


'''
'https://github.com/fchollet/keras/blob/master/keras/layers/normalization.py'
'https://github.com/ChihebTrabelsi/deep_complex_networks/blob/master/complexnn/norm.py'
'''
def sqrt_init(shape, dtype=None):
    value = (1 / np.sqrt(2)) * K.ones(shape)
    return value

def sanitizedInitGet(init):
    if init in ["sqrt_init"]:
        return sqrt_init
    else:
        return initializers.get(init)

def sanitizedInitSer(init):
    if init in [sqrt_init]:
        return "sqrt_init"
    else:
        return initializers.serialize(init)

def complex_standardization(input_centred, Vrr, Vii, Vri, layernorm = False, axis = -1):
    """Complex Standardization of input
    
    Arguments:
        input_centred -- Input Tensor
        Vrr -- Real component of covariance matrix V
        Vii -- Imaginary component of covariance matrix V
        Vri -- Non-diagonal component of covariance matrix V
    
    Keyword Arguments:
        layernorm {bool} -- Normalization (default: {False})
        axis {int} -- Axis for Standardization (default: {-1})
    
    Raises:
        ValueError: Mismatched dimensoins
    
    Returns:
        Complex standardized input
    """
    ndim = K.ndim(input_centred)
    input_dim = K.shape(input_centred)[axis] // 2
    variances_broadcast = [1] * ndim
    variances_broadcast[axis] = input_dim
    if layernorm:
        variances_broadcast[0] = K.shape(input_centred)[0]

    tau = Vrr + Vii
    delta = (Vrr * Vii) - (Vri ** 2)

    s = K.sqrt(delta)
    t = K.sqrt(tau + 2 * s)

    inverse_st = 1.0 / (s * t)
    Wrr = (Vii + s) * inverse_st
    Wii = (Vrr + s) * inverse_st
    Wri = -Vri * inverse_st

    broadcast_Wrr = K.reshape(Wrr, variances_broadcast)
    broadcast_Wri = K.reshape(Wri, variances_broadcast)
    broadcast_Wii = K.reshape(Wii, variances_broadcast)

    cat_W_4_real = K.concatenate([broadcast_Wrr, broadcast_Wii], axis=axis)
    cat_W_4_imag = K.concatenate([broadcast_Wri, broadcast_Wri], axis=axis)

    if (axis == 1 and ndim != 3) or ndim == 2:
        centred_real = input_centred[:, :input_dim]
        centred_imag = input_centred[:, input_dim:]
    elif ndim == 3:
        centred_real = input_centred[:, :, :input_dim]
        centred_imag = input_centred[:, :, input_dim:]
    elif axis == -1 and ndim == 4:
        centred_real = input_centred[:, :, :, :input_dim]
        centred_imag = input_centred[:, :, :, input_dim:]
    elif axis == -1 and ndim == 5:
        centred_real = input_centred[:, :, :, :, :input_dim]
        centred_imag = input_centred[:, :, :, :, input_dim:]
    else:
        raise ValueError(
            'Incorrect Batchnorm combination of axis and dimensions. axis '
            'should be either 1 or -1. '
            'axis: ' + str(axis) + '; ndim: ' + str(ndim) + '.'
        )
    rolled_input = K.concatenate([centred_imag, centred_real], axis=axis)

    output = cat_W_4_real * input_centred + cat_W_4_imag * rolled_input

    return output


def complex_batchnormalization(input_centred, Vrr, Vii, Vri, beta, gamma_rr, gamma_ri, gamma_ii, scale = True, center = True, layernorm = False, axis = -1):
    """Complex Batch Normalization
    
    Arguments:
        input_centred -- input data
        Vrr -- Real component of covariance matrix V
        Vii -- Imaginary component of covariance matrix V
        Vri -- Non-diagonal component of covariance matrix V
        beta -- Lernable shift parameter beta
        gamma_rr -- Scaling parameter gamma - rr component of 2x2 matrix
        gamma_ri -- Scaling parameter gamma - ri component of 2x2 matrix
        gamma_ii -- Scaling parameter gamma - ii component of 2x2 matrix
    
    Keyword Arguments:
        scale {bool} {bool} -- Standardization of input  (default: {True})
        center {bool} -- Mean-shift correction (default: {True})
        layernorm {bool} -- Normalization (default: {False})
        axis {int} -- Axis for Standardization (default: {-1})
    
    Raises:
        ValueError: Dimonsional mismatch
    
    Returns:
        Batch-Normalized Input
    """

    ndim = K.ndim(input_centred)
    input_dim = K.shape(input_centred)[axis] // 2
    if scale:
        gamma_broadcast_shape = [1] * ndim
        gamma_broadcast_shape[axis] = input_dim
    if center:
        broadcast_beta_shape = [1] * ndim
        broadcast_beta_shape[axis] = input_dim * 2

    if scale:
        standardized_output = complex_standardization(
            input_centred, Vrr, Vii, Vri,
            layernorm,
            axis=axis
        )

        # Now we perform th scaling and Shifting of the normalized x using
        # the scaling parameter
        #           [  gamma_rr gamma_ri  ]
        #   Gamma = [  gamma_ri gamma_ii  ]
        # and the shifting parameter
        #    Beta = [beta_real beta_imag].T
        # where:
        # x_real_BN = gamma_rr * x_real_normed +
        #             gamma_ri * x_imag_normed + beta_real
        # x_imag_BN = gamma_ri * x_real_normed +
        #             gamma_ii * x_imag_normed + beta_imag

        broadcast_gamma_rr = K.reshape(gamma_rr, gamma_broadcast_shape)
        broadcast_gamma_ri = K.reshape(gamma_ri, gamma_broadcast_shape)
        broadcast_gamma_ii = K.reshape(gamma_ii, gamma_broadcast_shape)

        cat_gamma_4_real = K.concatenate([broadcast_gamma_rr, broadcast_gamma_ii], axis=axis)
        cat_gamma_4_imag = K.concatenate([broadcast_gamma_ri, broadcast_gamma_ri], axis=axis)
        if (axis == 1 and ndim != 3) or ndim == 2:
            centred_real = standardized_output[:, :input_dim]
            centred_imag = standardized_output[:, input_dim:]
        elif ndim == 3:
            centred_real = standardized_output[:, :, :input_dim]
            centred_imag = standardized_output[:, :, input_dim:]
        elif axis == -1 and ndim == 4:
            centred_real = standardized_output[:, :, :, :input_dim]
            centred_imag = standardized_output[:, :, :, input_dim:]
        elif axis == -1 and ndim == 5:
            centred_real = standardized_output[:, :, :, :, :input_dim]
            centred_imag = standardized_output[:, :, :, :, input_dim:]
        else:
            raise ValueError(
                'Incorrect Batchnorm combination of axis and dimensions. axis'
                ' should be either 1 or -1. '
                'axis: ' + str(axis) + '; ndim: ' + str(ndim) + '.'
            )
        rolled_standardized_output = K.concatenate([centred_imag, centred_real], axis=axis)
        if center:
            broadcast_beta = K.reshape(beta, broadcast_beta_shape)
            return cat_gamma_4_real * standardized_output + cat_gamma_4_imag * rolled_standardized_output + broadcast_beta
        else:
            return cat_gamma_4_real * standardized_output + cat_gamma_4_imag * rolled_standardized_output
    else:
        if center:
            broadcast_beta = K.reshape(beta, broadcast_beta_shape)
            return input_centred + broadcast_beta
        else:
            return input_centred


class complex_BatchNormalization(tf.keras.layers.Layer):
    """Complex version of the real domain
    Batch normalization layer (Ioffe and Szegedy, 2014).
    Normalize the activations of the previous complex layer at each batch,
    i.e. applies a transformation that maintains the mean of a complex unit
    close to the null vector, the 2 by 2 covariance matrix of a complex unit close to identity
    and the 2 by 2 relation matrix, also called pseudo-covariance, close to the
    null matrix.
    # Arguments
        axis: Integer, the axis that should be normalized
            (typically the features axis).
            For instance, after a `Conv2D` layer with
            `data_format="channels_first"`,
            set `axis=2` in `complex_BatchNormalization`.
        momentum: Momentum for the moving statistics related to the real and
            imaginary parts.
        epsilon: Small float added to each of the variances related to the
            real and imaginary parts in order to avoid dividing by zero.
        center: If True, add offset of `beta` to complex normalized tensor.
            If False, `beta` is ignored.
            (beta is formed by real_beta and imag_beta)
        scale: If True, multiply by the `gamma` matrix.
            If False, `gamma` is not used.
        beta_initializer: Initializer for the real_beta and the imag_beta weight.
        gamma_diag_initializer: Initializer for the diagonal elements of the gamma matrix.
            which are the variances of the real part and the imaginary part.
        gamma_off_initializer: Initializer for the off-diagonal elements of the gamma matrix.
        moving_mean_initializer: Initializer for the moving means.
        moving_variance_initializer: Initializer for the moving variances.
        moving_covariance_initializer: Initializer for the moving covariance of
            the real and imaginary parts.
        beta_regularizer: Optional regularizer for the beta weights.
        gamma_regularizer: Optional regularizer for the gamma weights.
        beta_constraint: Optional constraint for the beta weights.
        gamma_constraint: Optional constraint for the gamma weights.
    # Input shape
        Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
    # Output shape
        Same shape as input.
    # References
        - [Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167)
    """
    def __init__(self,
                 axis=-1,
                 momentum=0.9,
                 epsilon=1e-4,
                 center=True,
                 scale=True,
                 beta_initializer='zeros',
                 gamma_diag_initializer='sqrt_init',
                 gamma_off_initializer='zeros',
                 moving_mean_initializer='zeros',
                 moving_variance_initializer='sqrt_init',
                 moving_covariance_initializer='zeros',
                 beta_regularizer=None,
                 gamma_diag_regularizer=None,
                 gamma_off_regularizer=None,
                 beta_constraint=None,
                 gamma_diag_constraint=None,
                 gamma_off_constraint=None,
                 **kwargs):

        super(complex_BatchNormalization, self).__init__(**kwargs)
        self.supports_masking = True
        self.axis = axis
        self.momentum = momentum
        self.epsilon = epsilon
        self.center = center
        self.scale = scale
        self.beta_initializer              = sanitizedInitGet(beta_initializer)
        self.gamma_diag_initializer        = sanitizedInitGet(gamma_diag_initializer)
        self.gamma_off_initializer         = sanitizedInitGet(gamma_off_initializer)
        self.moving_mean_initializer       = sanitizedInitGet(moving_mean_initializer)
        self.moving_variance_initializer   = sanitizedInitGet(moving_variance_initializer)
        self.moving_covariance_initializer = sanitizedInitGet(moving_covariance_initializer)
        self.beta_regularizer              = regularizers.get(beta_regularizer)
        self.gamma_diag_regularizer        = regularizers.get(gamma_diag_regularizer)
        self.gamma_off_regularizer         = regularizers.get(gamma_off_regularizer)
        self.beta_constraint               = constraints .get(beta_constraint)
        self.gamma_diag_constraint         = constraints .get(gamma_diag_constraint)
        self.gamma_off_constraint          = constraints .get(gamma_off_constraint)

    def build(self, input_shape):
        
        '''
        For complex convolutional neural networks
        input_shape     = (None, height, width, channel)
        len(input_shape = (None, height, width, channel))
        ndim            = 4
        dim             = 2, This is real channel and imag channel (self.axis = -1)
        '''
        ndim = len(input_shape)
        dim  = input_shape[self.axis]
        if dim is None:
            raise ValueError('Axis ' + str(self.axis) + ' of ' 'input tensor should have a defined dimension ' 'but the layer received an input with shape ' + str(input_shape) + '.')

        'For custom batch normalization layer, We need self.input_spec'
        self.input_spec = InputSpec(ndim = len(input_shape), axes = {self.axis: dim})

        'input_shape[-1] = 2 --> param_shape = (1, )'
        param_shape = (input_shape[self.axis] // 2,)

        if self.scale:
            self.gamma_rr   = self.add_weight(shape=param_shape, name='gamma_rr', initializer=self.gamma_diag_initializer, regularizer=self.gamma_diag_regularizer, constraint=self.gamma_diag_constraint)
            self.gamma_ii   = self.add_weight(shape=param_shape, name='gamma_ii', initializer=self.gamma_diag_initializer, regularizer=self.gamma_diag_regularizer, constraint=self.gamma_diag_constraint)
            self.gamma_ri   = self.add_weight(shape=param_shape, name='gamma_ri', initializer=self.gamma_off_initializer, regularizer=self.gamma_off_regularizer, constraint=self.gamma_off_constraint)
            self.moving_Vrr = self.add_weight(shape=param_shape, initializer=self.moving_variance_initializer, name='moving_Vrr', trainable=False)
            self.moving_Vii = self.add_weight(shape=param_shape, initializer=self.moving_variance_initializer, name='moving_Vii', trainable=False)
            self.moving_Vri = self.add_weight(shape=param_shape, initializer=self.moving_covariance_initializer, name='moving_Vri', trainable=False)
        else:
            self.gamma_rr   = None
            self.gamma_ii   = None
            self.gamma_ri   = None
            self.moving_Vrr = None
            self.moving_Vii = None
            self.moving_Vri = None

        'input_shape[self.aixs] == 2'
        if self.center:
            self.beta = self.add_weight(shape=(input_shape[self.axis],), name='beta', initializer=self.beta_initializer, regularizer=self.beta_regularizer, constraint=self.beta_constraint)
            self.moving_mean = self.add_weight(shape=(input_shape[self.axis],), initializer=self.moving_mean_initializer, name='moving_mean', trainable=False)
        else:
            self.beta = None
            self.moving_mean = None

        self.built = True

    def call(self, inputs, training=None):

        'real == [None, 256, 32, 1], imag == [None, 256, 32, 1]                        After concat axis == 3, inputs == [None, 256, 32, 2]'
        'input_shape == [None, 256, 32, 2], ndim == 4, reduction_axes == [0, 1, 2, 3], reduction_axes[-1] == 3 --> del reduction_axes[-1], reduction_axeis = [0, 1, 2]'
        input_shape     = K.int_shape(inputs)
        ndim            = len(input_shape)
        reduction_axes  = list(range(ndim))
        del reduction_axes[self.axis]
        input_dim       = input_shape[self.axis] // 2

        'mu is channel 2 (real, imag), Respectively mu_real, mu_imag'
        'broadcast_mu_shape = [1, 1, 1, 1] --> broadcast_mu_shape = [1, 1, 1, 2]'
        mu                            = K.mean(inputs, axis = reduction_axes)
        broadcast_mu_shape            = [1] * len(input_shape)
        broadcast_mu_shape[self.axis] = input_shape[self.axis]
        broadcast_mu                  = K.reshape(mu, broadcast_mu_shape)

        '[real, imag] vector - [mu_real, mu_imag] vector,   center_x = x - E[x]'
        if self.center:
            input_centred = inputs - broadcast_mu
        else:
            input_centred = inputs

        'centred_squared = [(r-mr), (i-mi)] * [(r-mr), (i-mi)] == [(r-mr)*(r-mr), (i-mi)*(i-mi)]'
        centred_squared = input_centred ** 2

        'Response to different types of BatchNormalization'
        if (self.axis == 1 and ndim != 3) or ndim == 2:
            centred_squared_real = centred_squared[ :, :input_dim]
            centred_squared_imag = centred_squared[ :, input_dim:]
            centred_real = input_centred[ :, :input_dim]
            centred_imag = input_centred[ :, input_dim:]
        elif ndim == 3:
            centred_squared_real = centred_squared[ :, :, :input_dim]
            centred_squared_imag = centred_squared[ :, :, input_dim:]
            centred_real = input_centred[ :, :, :input_dim]
            centred_imag = input_centred[ :, :, input_dim:]
        elif self.axis == -1 and ndim == 4:
            centred_squared_real = centred_squared[ :, :, :, :input_dim]
            centred_squared_imag = centred_squared[ :, :, :, input_dim:]
            centred_real = input_centred[ :, :, :, :input_dim]
            centred_imag = input_centred[ :, :, :, input_dim:]
        elif self.axis == -1 and ndim == 5:
            centred_squared_real = centred_squared[ :, :, :, :, :input_dim]
            centred_squared_imag = centred_squared[ :, :, :, :, input_dim:]
            centred_real = input_centred[ :, :, :, :, :input_dim]
            centred_imag = input_centred[ :, :, :, :, input_dim:]
        else:
            raise ValueError('Incorrect Batchnorm combination of axis and dimensions. axis should be either 1 or -1. ''axis: ' + str(self.axis) + '; ndim: ' + str(ndim) + '.')
        if self.scale:
            Vrr = K.mean(centred_squared_real, axis=reduction_axes) + self.epsilon
            Vii = K.mean(centred_squared_imag, axis=reduction_axes) + self.epsilon
            # Vri contains the real and imaginary covariance for each feature map.
            Vri = K.mean(centred_real * centred_imag, axis=reduction_axes)
        elif self.center:
            Vrr = None
            Vii = None
            Vri = None
        else:
            raise ValueError('Error. Both scale and center in batchnorm are set to False.')

        input_bn = complex_batchnormalization(input_centred, Vrr, Vii, Vri, self.beta, self.gamma_rr, self.gamma_ri, self.gamma_ii, self.scale, self.center, axis=self.axis)
        if training in {0, False}:
            return input_bn
        else:
            update_list = []
            if self.center:
                update_list.append(K.moving_average_update(self.moving_mean, mu, self.momentum))
            if self.scale:
                update_list.append(K.moving_average_update(self.moving_Vrr, Vrr, self.momentum))
                update_list.append(K.moving_average_update(self.moving_Vii, Vii, self.momentum))
                update_list.append(K.moving_average_update(self.moving_Vri, Vri, self.momentum))
            self.add_update(update_list, inputs)

            def normalize_inference():
                if self.center:
                    inference_centred = inputs - K.reshape(self.moving_mean, broadcast_mu_shape)
                else:
                    inference_centred = inputs
                return complex_batchnormalization(inference_centred, self.moving_Vrr, self.moving_Vii, self.moving_Vri, self.beta, self.gamma_rr, self.gamma_ri, self.gamma_ii, self.scale, self.center, axis=self.axis
                )

        # Pick the normalized form corresponding to the training phase.
        return K.in_train_phase(input_bn, normalize_inference, training=training)

    def get_config(self):
        config = {
            'axis': self.axis,
            'momentum': self.momentum,
            'epsilon': self.epsilon,
            'center': self.center,
            'scale': self.scale,
            'beta_initializer':              sanitizedInitSer(self.beta_initializer),
            'gamma_diag_initializer':        sanitizedInitSer(self.gamma_diag_initializer),
            'gamma_off_initializer':         sanitizedInitSer(self.gamma_off_initializer),
            'moving_mean_initializer':       sanitizedInitSer(self.moving_mean_initializer),
            'moving_variance_initializer':   sanitizedInitSer(self.moving_variance_initializer),
            'moving_covariance_initializer': sanitizedInitSer(self.moving_covariance_initializer),
            'beta_regularizer':              regularizers.serialize(self.beta_regularizer),
            'gamma_diag_regularizer':        regularizers.serialize(self.gamma_diag_regularizer),
            'gamma_off_regularizer':         regularizers.serialize(self.gamma_off_regularizer),
            'beta_constraint':               constraints .serialize(self.beta_constraint),
            'gamma_diag_constraint':         constraints .serialize(self.gamma_diag_constraint),
            'gamma_off_constraint':          constraints .serialize(self.gamma_off_constraint),
        }
        base_config = super(complex_BatchNormalization, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))


class complex_BatchNormalization2D (tf.keras.layers.Layer):

    def __init__ (self):
        super(complex_BatchNormalization2D, self).__init__()

        self.BatchNormalization = complex_BatchNormalization()

    def call (self, real, imag, training = True):

        concatenated_inputs  = tf.concat([real, imag], axis = 3)
        concatenated_outputs = complex_BatchNormalization()(concatenated_inputs, training = training)
        real = concatenated_outputs[ :, :, :, :1]
        imag = concatenated_outputs[ :, :, :, 1:]

        return real, imag


if __name__ == "__main__":

    real = tf.keras.layers.Input(shape = (512, 64, 1))
    imag = tf.keras.layers.Input(shape = (512, 64, 1))            

    real, imag = complex_Conv2D(1, (3, 3), (2, 2))(real, imag)
    print(real.shape, imag.shape)
    real, imag = complex_BatchNormalization2D()(real, imag, True)
    print(real.shape, imag.shape)